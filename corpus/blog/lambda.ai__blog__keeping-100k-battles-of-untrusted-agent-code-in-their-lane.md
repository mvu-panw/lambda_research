# Keeping 100k battles of untrusted agent code in their lane

Source: https://lambda.ai/blog/keeping-100k-battles-of-untrusted-agent-code-in-their-lane

Skip to main content

# Keeping 100k battles of untrusted agent code in their lane

 July 30, 2026

 • 13 min read

In March 2026, Lambda ran AgentBeats, an AI agent security competition in which teams submit two kinds of agents: an attacker that tries to manipulate a target LLM into doing something harmful, and a defender that tries to stay helpful while refusing the trap (check the final leaderboard here). Our platform pairs them, runs the battle, and scores the outcome. The agents are graded on how effectively they subvert the system, which means the platform's job is to stay correct and on schedule while the code it hosts is trying to break things.

The short version: 48 rounds over 27 days, around 100k battles, 22 teams, 574 submissions on a pool of at most four NVIDIA HGX H100 GPUs. The part I want to tell you about most: we added GPUs during live rounds, with a single command, without dropping a battle.

Note: The "security" described in this post is the topic the agents were competing in ("attacker vs. defender agents"), not a property claimed for the proposed platform itself. I'm an ML person, not a systems security expert, and the containment described below (Docker networks, an egress allowlist, and resource caps) doesn't describe a properly sandboxed system. It was sized for a month-long competition with modest prizes and a known participant pool and used a small, easy-to-control model, gpt-oss 20B.

The timing of this write-up isn't intentional, but it couldn't be more up to date: just as I was finishing this post, OpenAI disclosed an incident in which models under evaluation escaped an isolated environment through a zero-day in its package-registry proxy, the same kind of egress path I describe below, and went on to compromise production infrastructure to cheat on the benchmark. Against that class of adversary, nothing in this post would hold. For the competition described here, it didn't need to. If a container escape would ruin your day, you want microVM isolation such as Firecracker or gVisor and a real threat model. This post has neither. What it has is the ops story: how we kept 100k battles of code we didn't trust on schedule and on four GPUs, for a month.

More details:

- 48 rounds, twice daily, March 6 to April 1st, 2026 for 22 teams and 574 total submissions

- Up to 2,098 battles in a single round (the final round of Apr 1st)

- Median round took ~10.3 hours, ranging from 7.6 hours on a light day to 16.8 hours on a heavy one (across the 48 rounds with complete timing)

- Due to rising participant numbers throughout the competition, we hot-loaded additional GPUs mid-round, with zero battles dropped

- Every round was completed, scored, and redeployed on schedule so teams could keep submitting late, even broken agents, without threatening the round's integrity or the leaderboard

The subject of this post is the infrastructure behind those numbers: independent per-GPU vLLM replicas, a single Caddy container that handles all network traffic (in and out), a concurrency limiter that resizes at runtime so a GPU can be folded in mid-round, a rate-limiter sidecar, and a serverless AWS submission path.

## But first, assume the code hates you

The defining property of this system: it executes untrusted, adversarial, financially-incentivized (we gave out prizes) code on shared hardware. Everything below is downstream of three problems:

- Cost. The GPU budget is fixed: at most four NVIDIA HGX H100 GPUs, with one as a starting point and three additional held in reserve, launched dynamically as demand increased throughout the competition. Although technically possible using the Lambda Cloud API, we didn't set up any autoscaling. If a round runs longer than the interval to the next round, the schedule degrades.

- Containment. Agents shouldn't access the internet, other battles, or the AWS account holding submissions and results. Not because we built an escape-proof sandbox (see note at the top) but because removing the easy paths keeps the competition fair and the blast radius small.

- Fairness. No agent may starve another agent's GPUs, and no defender agent may carry state from one round to the next (even a cached jailbreak, or a stored opponent prompt, would skew the competition toward the code that cracked the container).

Here's what the system looks like with that framing set.

## System shape

The platform is split into three planes because it serves three workloads with different cost and uptime profiles.

Ingestion is serverless because submissions arrive in bursts and the path sits idle most of the day: API Gateway, an AWS Lambda that validates each upload (size caps, a 100:1 compression-ratio check for zip bombs, path-traversal and extension filtering), DynamoDB for state, and S3 for submissions, results, and the frontend. The important detail here is the credential the evaluation host uses to pull that data down.

EvaluatorUser is read-only on the submissions bucket and the teams table. The host that runs the untrusted code can't alter a submission or a team record (i.e., the machine most likely to be compromised holds the weakest key, though it can still read every submission, a tradeoff that we accept here).

## Four replicas instead of tensor parallelism for GPU serving

The model we’re using for the competition is OpenAI’s gpt-oss-20b, served with vLLM. Four 80 GB NVIDIA HGX H100 GPUs invite the obvious layout: --tensor-parallel-size 4, one logical endpoint, weights split across all cards. We didn't do that. Each GPU runs its own complete, independent vLLM on :8000 with a full copy of the weights. Since the model fits on a single card in the served precision, we can also run replicas and scale dynamically instead. This is helpful because active participants vary over the competition, and in our case, they grew.

Why this layout worked well in our case:

- A new replica joins the rotation in seconds. That's what makes hot-loading mid-round possible and easy (see description below).

- Failure stays local. If one vLLM wedges, the others keep serving. Under tensor parallelism, one problem (bug or hardware error) may take the whole endpoint down.

- Of course, throughput scales linearly with GPUs. Four replicas serve four times the concurrent battles.

It also changes the economics: instead of a fixed layout with mostly idle GPUs, the pool becomes dynamic as cards get added when rounds run long and spend stays matched to demand.

## One container between the agents and everything else

Battle containers run on a Docker network named agentbeats-isolated, which has no route to the internet. One Caddy instance straddles that boundary and does four things:

- Load-balances the GPUs. Caddy reverse-proxies the vLLM backends with lb_policy round_robin. Agents connect to one stable internal address; Caddy distributes requests across the healthy replicas. 

- Health-checks the backends. Every 10 seconds, Caddy probes each backend's /health with a 5-second timeout and drops unhealthy upstreams from rotation.
reverse_proxy $UPSTREAMS {
    lb_policy round_robin 
    health_uri /health 
   health_interval 10s 
    health_timeout 5s 
    transport http { 
       dial_timeout 30s 
       response_header_timeout 600s # reasoning models hold connections for minutes   
      read_timeout 600s 
       write_timeout 600s 
   } 
    flush_interval -1 # stream tokens through, do not buffer 
}The 600-second transport timeouts exist because a reasoning model mid-generation can hold a connection open for minutes; flush_interval -1 passes tokens straight through rather than buffering the stream.

- Is the only path to install packages. Agent containers need PyPI at startup. "Needs PyPI" is not "needs the internet," so Caddy also runs a forward proxy on :3128 with an allowlist:
:3128 { 
   forward_proxy { 
       acl { 
           allow *.pypi.org 
           allow *.pythonhosted.org 
           allow *.astral.sh 
           deny all 
       } 
       hide_ip 
       hide_via 
   } 
}

An agent can pip install its dependencies and nothing else. That closes the casual routes out. In light of recent events: a package registry is itself also an exfiltration channel, as anyone can publish a package, and, as the incident linked at the top shows, even the proxy in front of it can be the hole. That's the class of attacker this setup wouldn’t defend against.

-  Reloads without dropping connections. This is what makes runtime rescaling possible, covered next.

The reverse proxy listens on :8080, the forward proxy on :3128, and Caddy's admin API stays bound to localhost:2019 so nothing on the evaluation network can reach it.

## Adding a GPU mid-round

We started with a single NVIDIA HGX H100 GPU in steady state and added a second, a third, and a fourth one by one as the competition scaled past its compute limits. The “pressure” here is defined by the schedule: rounds fire twice a day, so a 16.8-hour round on the steady-state pool can eat the next cutoff and push the whole competition behind. The hot-loadable cards are the slack that keeps a long round from cascading into the following one.

For us, folding in a card was one command:

python -m backend add-backend http://<gpu-3-ip>:8000/v1

The implementation does three things in a specific order:

- Health-check the new backend by calling /v1/models with the API key. If it's not serving, the operation aborts without changing anything.

- Reload Caddy before anything else learns the GPU exists. The Caddyfile is rewritten with the new upstream and reloaded over the admin socket (with a fallback to a container restart and /health poll if the reload API is unavailable). Caddy is now willing to route to the added card.

- Write .env last. The running evaluation process watches this file for changes.

Inside the orchestrator, a daemon thread polls .env every 5 seconds. When VLLM_URLS changes, it recomputes the worker budget and resizes a live concurrency limiter:

class ConcurrencyGate: 
   """Dynamic concurrency limiter. Supports resizing at runtime.""" 
   def __enter__(self): 
       with self._cond: 
          while self._active >= self._max: 
              self._cond.wait() 
          self._active += 1 
       return self 

   def resize(self, new_max): 
       new_max = max(1, new_max) 
       with self._cond: 
          old, self._max = self._max, new_max 
          if new_max > old: 
             self._cond.notify_all() # wake waiters to take the new slots

Every battle runs inside with gate:. The budget is PARALLEL_WORKERS_PER_BACKEND × backends: we found that four workers per GPU works well for our workload, so one GPU instance allows four concurrent battles and four GPU instances allow sixteen. When the watcher calls resize(12), four queued battles waiting on _cond.wait() wake up and start.

This is the part I like most: the ordering is the whole trick. Caddy is reloaded before .env is written, so routing exists before the worker pool scales up. Do it the other way around, and the watcher dispatches battles to a GPU instance Caddy has never heard of: connection refused, battles failed. Removing a backend runs the same sequence in reverse: drain it from Caddy first, then let the watcher shrink the gate so no new battle is routed to a card on its way out.

So, the hard GPU ceiling became a runtime parameter, held together by a 5-second file poll.

## Inside a single battle

A battle is five containers on agentbeats-isolated, and the agents never address a GPU directly.

The five containers are:

- a containerized attacker agent (listening on :9021)

- a containerized defender agent (:9020)

- the shared Caddy proxy

- the shared rate-limiter sidecar

- an orchestrator that drives the scenario, manages each agent's call budget, and talks to all of them

The attacker and defender receive an OPENAI_BASE_URL that points at the rate limiter, which sits in front of Caddy, which sits in front of vLLM.

Fairness is enforced by a separate process. The agentbeats-ratelimiter is its own sidecar on :8081. At battle start, the orchestrator registers the battle and the limiter mints per-role tokens; each agent receives a key shaped like token:actual_key. The limiter splits it, counts requests against the token, and returns HTTP 429 when an agent exceeds its per-round budget, which is the same status the agent's LLM client already handles.

To ensure fairness across teams while keeping resources low, we capped the “LLM call budget” to 4 calls per response per role. Admin operations on the limiter (such as registering, resetting, and inspecting counts) require a separate admin token known only to the orchestrator, so an agent can't reset its own counter.

Additionally, the defender is wiped after every request to ensure the competition isn't skewed toward defenders (otherwise, defenders could block all future requests if they detected an attack successfully).

Talking about fairness, and since this competition is about pairwise battles, we need to explain what happens when one side errors. If an agent crashes or times out, that side forfeits the battle, but the opponent is not credited with a win. The collector counts crashes and timeouts per agent, separately from wins and losses, so a battle that ends because one container died is booked as a failure on that side rather than a victory for the other.

A failing agent, therefore, can't distort an opponent's win rate: a crash is attributed to whoever produced it and is scored as a forfeit, not an outcome. In our frontend, participants could see how often their agent was crashing. However, we couldn't allow them to see the exact error message so no competition data leaked. For debugging purposes, we've provided them with the battle code so they could test their submissions beforehand locally.

The orchestrator applies resource limits and a per-call wall-clock timeout charged to whichever agent exceeded it. For the competition, we defaulted to 2 GB of memory, a 256-PID cap (to bound fork bombs), and a 240-second call timeout.

## A round, start to finish

The evaluator is one long-running process (uv run python -m backend run-forever --at 11:59,23:59 ) that fires twice a day, at UTC cutoffs chosen to match an Anywhere-on-Earth submission deadline. Each cutoff runs the same pull-compute-push sequence: pull the day's submissions from S3 using the read-only credential, run the matchups, then push the results back to S3 and DynamoDB, and redeploy the frontend.

The matchups are not all-vs-all, which would be quadratic and blow the target compute budget quickly. With TOP_K=10, every attacker faces the top 10 defenders and every defender the top 10 attackers, which bounds a round against a fixed pool. The current top-K lists were marked on the leaderboard at all times.

Two details were important since the system ran mostly unattended for two weeks. First, a helpfulness check: before a defender's score counts, the orchestrator runs it on a sample of benign scenarios and verifies that it remains helpful.

A defender that refuses everything is trivially unbeatable and useless, so it fails the round. A defender that fails doesn't drop out; the pipeline reuses that team's last submission that passed that check, so a regression cannot quietly remove a team from competition.

Second, a long-lived process will eventually miss a cutoff; maybe a reboot, or a wedged round. Our tooling run-forever supported --catchup-schedule-since-date, which replays every missed cutoff in order before rejoining the live schedule.

## What I'd reuse

Independent of the AgentBeats specifics, four decisions generalize to anyone running untrusted or expensive workloads on GPUs.

- Make fixed capacity resizable, and keep the router ahead of the pool. A runtime-resizable concurrency limiter and a file-watching daemon turned a hard GPU ceiling into a runtime parameter.

- Put all network plumbing in one reloadable chokepoint. Caddy was the load balancer, health checker, sole egress, and package gatekeeper. The containment itself was only a network with no route out and an allowlist ending in deny all, but keeping it in one process meant one config to read during development when something looked wrong.

- Match the infrastructure to the load. Bursty, idle-most-of-the-day ingestion belongs on serverless; steady, stateful, hours-long evaluation belongs on a long-lived host.

- Give every rule its own process, and every process the least it needs. The referee shouldn't run inside the game: a standalone rate limiter with an admin token the agents never see, a defender wiped after every request, and a read-only data credential on the most-exposed host. Small decisions that kept the scores trustworthy.

To be precise about what this design actually defends against: a competitor hogging the GPU, casually beaconing out, carrying state across rounds, or skewing a score. What it doesn't defend against: container escapes, kernel exploits, package-registry abuse, or anyone willing to invest more than the prize money is worth (the class of adversary from the incident at the top).

For a month-long competition with a known participant pool, that was the right trade. The real result is a system hosting adversarial code that ran unattended for two weeks and stayed uneventful. Uneventfulness was the goal.

Check the final leaderboard here and read more Lambda research here.

## AUTHORED BY

 David Hartmann

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
