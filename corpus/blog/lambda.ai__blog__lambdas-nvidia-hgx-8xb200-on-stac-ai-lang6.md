# Lambda’s NVIDIA HGX B200 on STAC-AI™ LANG6

Source: https://lambda.ai/blog/lambdas-nvidia-hgx-8xb200-on-stac-ai-lang6

Skip to main content

# Lambda’s NVIDIA HGX B200 on STAC-AI™ LANG6

 May 19, 2026

 (Updated on May 21, 2026)

 • 39 min read

## What the numbers mean for financial services

### Executive summary

Lambda is the first to publish an audited STAC-AI™ LANG6 result on NVIDIA HGX B200, with independently verified performance data that Financial Services Industry (FSI) infrastructure teams can use to make a concrete infrastructure decision: whether NVIDIA HGX B200 unlocks workloads, concurrency levels, or model sizes that your current generation GPU cannot support. For teams running LLM inference on NVIDIA H200 GPUs today, or evaluating whether to do so, these results answer the question directly.

- 

Latency that doesn't break under load. At 165 req/s for the 8B model, the NVIDIA 8×H200 NVL reached a median latency of 15.5s, effectively saturating. NVIDIA HGX B200 handled the same load at a median latency of 1.39s. For trading desks and research teams, this is the difference between a tool analysts actively use during market hours and one they abandon when the desk is busy. It means you can serve your entire team concurrently on a single node, at latencies that feel instant, without overprovisioning or load shedding.

- A 70B model, fully interactive, at production concurrency. At 20 req/s, NVIDIA HGX B200 delivered 0.095s Time-To-First-Token (TTFT)  and a 3.45s median latency, versus NVIDIA 8×H200 NVL’s 0.522s TTFT and 21.4s median latency at the same load. NVIDIA HGX B200 can serve the model with 0.335s TTFT at  75 req/s, a load the NVIDIA 8×H200 NVL couldn’t sustain. For FSI teams that need reasoning-grade model quality for compliance review or client-facing output but have held back due to latency concerns. A 70B model is now viable as an interactive, production tool, not just a batch-only workload.

- 

Batch throughput that changes overnight economics. For the 8B model, NVIDIA HGX B200 delivered 52,823 wps, more than double the NVIDIA 8×H200 NVL. For the 70B model, it delivered 12,040 wps, 3.59× the NVIDIA 8×H200 NVL. For the 70B model at Long-context, it delivers 350 wps versus 132 wps on NVIDIA 8×H200 NVL. For compliance and operations teams running overnight batch review, this means the same job window processes more documents, or the same document volume completes in a shorter window, without scaling infrastructure.

- 

Long-context performance that improves under pressure, not degrades. On E5a long-context workloads, NVIDIA 8×H200 NVL hit 36.2s latency at 2.4 req/s, saturating on the kinds of dense regulatory documents compliance teams process daily. NVIDIA HGX B200 held at 3.31s at the same load and extended to 5.6 req/s, while the NVIDIA 8×H200 NVL couldn’t follow. Batch throughput on long-context workloads improved by 133%, from 954 wps to 2,220 wps. For any team processing documents longer than a few thousand tokens, this result justifies the infrastructure decision.

 | Stat
 | NVIDIA HGX B200
 | NVIDIA 8xH200 NVL baseline
 | Delta
 | What it means

 | 8B batch throughput, E4a
 | 52,823 wps
 | 23,607 wps
 | +124%
 | More than double the NVIDIA 8xH200 NVL batch throughput for 8B

 | 70B batch throughput, E4b
 | 12,040 wps
 | 3,351 wps
 | +259%
 | 3.6× NVIDIA 8×H200 NVL throughput on a full 70B model

 | 8B median latency @ 165 req/s, E4a
 | 1.39s
 | 15.5s
 | –91%
 | NVIDIA 8×H200 NVL was saturating at this load; NVIDIA HGX B200 handled it cleanly

 | 70B TTFT @ 20 req/s, E4b

 | 0.095s
 | 0.522s
 | –82%
 | Sub-100ms first token on a 70B model at production load

* Baseline figures are from the audited STAC-AI™ LANG6 result on HPE ProLiant DL380a Gen12 with NVIDIA 8×H200 NVL (docs.stacresearch.com/HPE250907b). Lambda is the first to publish STAC-AI™ LANG6 results on NVIDIA HGX B200.

### Why benchmark LLM inference for finance at all?

Generic AI benchmarks assess an AI model’s intelligence. Financial services customers need to know how quickly, reliably, and at what cost a full infrastructure stack can serve that model under realistic financial workloads, summarizing regulatory filings, surfacing risk signals, answering analyst questions in real time, and running batch compliance reviews overnight. That requires an entirely different test.

STAC-AI™ LANG6 is that test. Designed by quants and technologists from leading financial institutions, it's the industry standard for LLM inference performance in capital markets contexts, and an independently audited STAC number is worth more to a risk-conscious FSI buyer than any vendor claim.

### The three metrics that matter

STAC-AI LANG6 produces three categories of official metrics. Here’s what each one actually means for a financial services deployment.

#### 1. Latency: “How fast does a user get a response?”

STAC measures two latency metrics: time-to-first-token (TTFT), the time from sending a request to receiving the first word of output, and total response time, the full end-to-end wait. It also tests whether token streaming stays above human reading speed throughout. For a trading analyst waiting on an earnings summary, a 200 ms reaction time feels instant. A 2-second wait feels like a broken system. User response speed directly impacts real business value.

#### 2. Throughput: “How many requests can we handle simultaneously?”

Throughput is measured in words per second for both interactive mode and batch mode. This is what determines whether the system holds up when the entire desk is querying during earnings season or when a compliance batch job needs to finish inside a regulatory window.

#### 3. Cost efficiency: “What does it cost to run at scale?”

For public cloud, efficiency metrics are based on published pricing, expressed in US dollars per hour to rent the SUTs at the time of testing. To contextualize performance against cost, we normalize throughput by price, yielding words per USD as the cost efficiency measure.

### FSI benchmark use cases

#### Use case 1: trading desks
Real-time filing and earnings analysis 

Picture an equity research team during earnings season. Twelve companies report before the market opens. Each 10-K or earnings transcript is tens of thousands of words. The analyst needs a structured summary, revenue drivers, risk factors, and management commentary on macro before the opening bell.

This is exactly the EDGAR4a interactive workload, and it’s where the choice between 8B and 70B becomes concrete. The relevant questions are:

- Can the system respond quickly enough so analysts don’t have to sit and wait? (Latency / Reaction time)

- Can it handle multiple analysts querying simultaneously without degrading? (Throughput under concurrency)

- Can it sustain token streaming above reading speed so the UI doesn’t feel sluggish? (Output profile)

- Does the 70B model’s higher reasoning quality justify its latency cost for this workflow? (Model selection trade-off)

On NVIDIA HGX B200, the 8B model sustained 165 req/s with a median latency of 1.39s and TTFT of 0.0375s. This is a 91% latency improvement over NVIDIA 8×H200 NVL at the same load, where the NVIDIA 8×H200 NVL hit a median latency of 15.5s. At 320 req/s , the NVIDIA HGX B200 delivered 53,469 wps at 4.48s latency. For the 70B model, the NVIDIA HGX B200 system serves 20 req/s with a median TTFT of 0.095s and a latency of 3.45s, versus the NVIDIA 8×H200 NVL’s median TTFT of 0.522s and a latency of 21.4s at the same load. That is not a marginal improvement; the NVIDIA 8×H200 NVL was saturating, and NVIDIA HGX B200 was operating comfortably within its range.

The practical implication: a team can go from filing release to actionable summary in seconds with the 8B model, or opt for deeper analytical quality with the 70B model when the question demands it, on Lambda’s NVIDIA HGX B200, without investing in a full rack-scale system. The benchmark gives you the concrete performance improvements of that upgrade so you can make the call deliberately rather than by instinct.

#### Use case 2: risk and compliance teams
Regulatory compliance document review 

Compliance teams operate in a different regime. The priority isn’t millisecond reaction time, it’s volume. A risk team tasked with reviewing hundreds of counterparty disclosures or flagging clauses across a portfolio of contracts must process large documents in batches, overnight or over a defined window, and needs confidence that the system won’t run out of memory mid-job.

While the EDGAR4a benchmark focuses on interactive workloads, the compliance use case is where the 70B model’s advantage over 8B becomes most defensible. Longer documents, more nuanced clause interpretation, and lower tolerance for hallucination all point toward the larger model. The benchmark results give you the data to quantify exactly what that choice costs in throughput and latency terms, so that the decision can be made on evidence, not assumption.

- How many documents can the system process per hour at 8B vs 70B? (Throughput v.s. quality trade-off)

- Can it handle the long context windows of dense regulatory documents without OOM errors? (Memory capacity, 192 GB HBM3e per NVIDIA Blackwell GPU vs 140 GB on NVIDIA 8×H200 NVL is directly relevant here)

- What is the operational energy cost over a multi-hour batch run at each model size? (Energy efficiency)

On batch workloads, NVIDIA HGX B200 results are the strongest in the dataset. 8B E5a batch throughput reached 2,220 wps, compared with an NVIDIA 8×H200 NVL baseline of 954 wps, a 133% improvement. On interactive E5a workloads, NVIDIA HGX B200 handled 2.4 req/s at 3.31s median latency, versus the NVIDIA 8×H200 NVL's 36.2s at the same load, and extended to 5.6 req/s, where the NVIDIA 8×H200 NVL couldn’t sustain load at all. The 70B E5b batch reached 350 wps against an NVIDIA 8×H200 NVL baseline of 132 wps, a 165% improvement. The long-context batch gap is directly attributable to the NVIDIA Blackwell GPU memory architecture: 192 GB HBM3e per GPU at 8 TB/s allows the system to hold long-context requests in fast memory, which the NVIDIA 8×H200 NVL must offload, compounding throughput advantages as document length increases.

The 192 GB of HBM3e per GPU on NVIDIA HGX B200 is not an accident; it means the system can hold longer context windows in fast memory, avoiding the latency penalty of offloading that constrains memory-limited GPUs on large-document tasks. For compliance workloads where documents are long, and context window pressure is real, this architectural advantage directly translates into throughput.

#### Use case 3: wealth management / private banking
AI-assisted client advisory and report generation 

Wealth managers and private bankers face a different AI deployment challenge from trading desks or compliance teams. The output is client-facing. This includes investment commentary, portfolio reviews, and market outlooks, which means quality matters as much as speed, and the model needs to handle personalized context (a client’s holdings, risk profile, prior correspondence) alongside market data.

This is a 70B workload by default. The reasoning quality gap between 8B and 70B is most visible when the model needs to synthesize multiple data sources into coherent, nuanced prose, the kind of output a relationship manager would put their name on. The benchmark results answer the infrastructure question that makes or breaks the deployment:

- Can a 70B model serve multiple advisors simultaneously without each waiting seconds for a response? (Interactive throughput and reaction time under concurrency)

- Can it handle the mixed long-short context of client files alongside real-time market inputs? (Memory capacity and context switching)

- What does running this at scale across a large advisory team cost in energy and compute? (Energy efficiency for TCO planning)

The 70B results on E4b are directly relevant here: 20 req/s sustained with 0.095s reaction time. This is fast enough that an advisor’s workflow is not interrupted waiting for the model, and well within the threshold at which AI-assisted generation feels native rather than bolted-on. The 82% margin over NVIDIA 8xH200 NVL’s 0.522s baseline at peak load means there is headroom to scale concurrent advisory users without hitting a latency wall.

The practical implication for a private bank or wealth platform: a single NVIDIA HGX B200 instance can serve a meaningful number of concurrent advisors with a full 70B model, delivering draft commentary, summarizing client portfolios against market conditions, and flagging relevant filings, without the infrastructure footprint of a rack-scale deployment. That changes the unit economics of AI-assisted advisory at the team or branch level.

### What we tested

#### The hardware: NVIDIA HGX B200

NVIDIA HGX B200 is NVIDIA’s Blackwell-generation data center GPU, designed for maximum inference throughput on large language models. NVIDIA HGX B200 comprises 8x Blackwell GPUs. Each GPU is equipped with 192 GB of HBM3e memory with 8 TB/s of memory bandwidth, 1.4× the memory and 1.7× the bandwidth of the NVIDIA 8×H200 NVL (141 GB / 4.8 TB/s), alongside fifth-generation NVIDIA Tensor Cores supporting NVFP4 precision for up to 72 petaFLOPS of dense compute. NVIDIA Blackwell GPUs are interconnected via NVIDIA NVLink 5 at 1.8 TB/s per GPU for high-speed multi-GPU communication.

 | 

Specification

 | 

NVIDIA Blackwell GPU specs in HGX B200 system

 | 

GPU architecture

 | 

Blackwell 

 | 

HBM3e memory

 | 

192 GB

 | 

Memory bandwidth

 | 

8 TB/s

 | 

NVFP4 dense compute

 | 

9 PFLOPS

 | 

NVLink bandwidth (5th gen)

 | 

1.8 TB/s

 | 

vs NVIDIA H200 GPU memory bandwidth

 | 

1.7× (8 TB/s vs 4.8 TB/s)

 | 

vs NVIDIA H200 GPU HBM3e memory

 | 

1.4× (192 GB vs 141 GB)

#### The model and software stack

We ran both Llama 3.1 8B Instruct and Llama 3.1 70B Instruct, served via NVIDIA TensorRT-LLM (TRT-LLM), the same inference engine used in NVIDIA’s own STAC-AI submissions and the reference stack recommended by both STAC and NVIDIA for this benchmark. TRT-LLM compiles and optimizes the model graph specifically for the target GPU architecture, squeezing out latency and throughput that general-purpose serving frameworks leave on the table.

Testing both model sizes is deliberate. The 8B model is the workhorse of FSI RAG deployments, fast enough for interactive workloads, and capable of document summarization and Q&A on structured financial text. The 70B model represents the other end of the spectrum: higher reasoning quality and longer effective context, at greater compute cost. Publishing results for both provides FSI teams with a concrete basis for the trade-off decision, rather than requiring them to extrapolate from a single data point.

#### The datasets: EDGAR4 and EDGAR5 variants

STAC-AI LANG6 uses datasets derived from real SEC EDGAR 10-K filings, the kind of documents your analysts and compliance teams read every quarter. We tested across four dataset variants:

- EDGAR4a: Medium-length prompts from 10-K filings, modeling interactive real-time summarization requests. Used for Llama 3.1 8B.

- EDGAR4b: The same EDGAR4 prompt style at the sequence length distribution calibrated for 70B model evaluation. Used for Llama 3.1 70B.

- EDGAR5a: Longer, denser prompts requiring extended context windows, the closest proxy to large-document review tasks. Used for 8B.

- EDGAR5b: The EDGAR5 long-context profile calibrated for 70B. Batch-only. Used for Llama 3.1 70B.

The letter suffix (a vs b) denotes a fixed input/output sequence-length distribution tuned to the model size under test; this is what allows apples-to-apples comparison across hardware submissions for each model. The EDGAR4 variants focus on interactive latency and throughput; the EDGAR5 variants stress-test the system under maximum context pressure, where the NVIDIA 8xHGX B200’s 192 GB HBM3e per GPU becomes a concrete architectural advantage.

### NVIDIA HGX B200 results

All response and reaction times are in seconds. Batch throughput is in words per second. Baseline refers to the independently audited STAC-AI™ LANG6 result on HPE ProLiant DL380a Gen12 with NVIDIA 8×H200 NVL [1].

#### Benchmark metrics

Llama 3.1 8B — E4a

 | 

Load (req/s)

 | 

NVIDIA HGX B200 throughput (wps)

 | 

NVIDIA 8×H200 NVL throughput (wps)

 | 

Throughput Δ

 | 

NVIDIA HGX B200 latency (s)

 | 

NVIDIA 8×H200 NVL latency (s)

 | 

Latency Δ

 | 

NVIDIA HGX B200 TTFT (s)

 | 

NVIDIA 8×H200 NVL TTFT (s)

 | 

TTFT

Δ

 | 

116

 | 

19,646

 | 

18,410

 | 

+6.7%

 | 

1.05

 | 

2.73

 | 

−62%

 | 

0.0357

 | 

0.076

 | 

−53%

 | 

152

 | 

25,729

 | 

23,914

 | 

+7.6%

 | 

1.29

 | 

8.08

 | 

−84%

 | 

0.0363

 | 

0.124

 | 

−71%

 | 

165

 | 

27,919

 | 

25,314

 | 

+10.3%

 | 

1.39

 | 

15.5

 | 

−91%

 | 

0.0375

 | 

0.191

 | 

−80%

 | 

320 (NVIDIA HGX B200 only)

 | 

53,469

 | 

n/a

 | 

—

 | 

4.48

 | 

n/a

 | 

—

 | 

0.0807

 | 

n/a

 | 

—

 | 

BATCH

 | 

52,823

 | 

23,607

 | 

+124%

 | 

—

 | 

—

 | 

—

 | 

—

 | 

—

 | 

—

Llama 3.1 8B — E5a

 | 

Load (req/s)

 | 

NVIDIA HGX B200 throughput (wps)

 | 

 NVIDIA 8×H200 NVL throughput (wps)

 | 

Throughput Δ

 | 

NVIDIA HGX B200 latency (s)

 | 

NVIDIA 8×H200 NVL latency (s)

 | 

Latency Δ

 | 

NVIDIA HGX B200 TTFT (s)

 | 

NVIDIA 8×H200 NVL TTFT (s)

 | 

TTFT 
Δ

 | 

1.68

 | 

661

 | 

643

 | 

+2.8.0% |

 | 

2.97

 | 

8.76

 | 

−66%

 | 

0.988

 | 

2.72

 | 

−64%

 | 

2.16

 | 

848

 | 

816

 | 

+3.9%

 | 

3.15

 | 

17.40

 | 

−82% 

 | 

1.01

 | 

3.30

 | 

−69%

 | 

2.4

 | 

942

 | 

797

 | 

+18.2%

 | 

3.31

 | 

36.20

 | 

−91%

 | 

1.02

 | 

4.59

 | 

−78%

 | 

5.6 (NVIDIA HGX B200 only)

 | 

2,002

 | 

n/a

 | 

—

 | 

44

 | 

n/a

 | 

—

 | 

3.16

 | 

n/a

 | 

—

 | 

BATCH

 | 

2,220

 | 

954

 | 

+133%

 |  
 | 

—

 | 

—

 |  
 | 

—

 | 

—

Llama 3.1 70B — E4b

 | 

Load (req/s)

 | 

NVIDIA HGX B200 throughput (wps)

 | 

NVIDIA 8×H200 NVL throughput (wps)

 | 

Throughput Δ

 | 

NVIDIA HGX B200 latency (s)

 | 

NVIDIA 8×H200 NVL latency (s)

 | 

Latency Δ

 | 

NVIDIA HGX B200 TTFT (s)

 | 

NVIDIA 8×H200 NVL TTFT (s)

 | 

TTFT 

Δ

 | 

16

 | 

2,505

 | 

2,447

 | 

+2.4%

 | 

3.25

 | 

13.6

 | 

−76%

 | 

0.0932

 | 

0.377

 | 

−75%

 | 

18

 | 

2,821

 | 

2,745

 | 

+2.8%

 | 

3.34

 | 

16.1

 | 

−79%

 | 

0.0937

 | 

0.426

 | 

−78%

 | 

20

 | 

3,131

 | 

2,967

 | 

+5.5%

 | 

3.45

 | 

21.4

 | 

−84%

 | 

0.095

 | 

0.522

 | 

−82%

 | 

75 (NVIDIA HGX B200 only)

 | 

11,213

 | 

n/a

 | 

—

 | 

19

 | 

n/a

 | 

—

 | 

0.335

 | 

n/a

 | 

—

 | 

BATCH

 | 

12,040

 | 

3,351

 | 

+259%

 | 

—

 | 

—

 | 

—

 | 

—

 | 

—

 | 

—

Llama 3.1 70B — E5b

 | 

Load (req/s)

 | 

NVIDIA HGX B200 throughput (wps)

 | 

NVIDIA 8xH200 NVL throughput (wps)

 | 

Throughput \u0394

 | 

BATCH

 | 

350

 | 

132

 | 

+165%

### 
Reading the results

Across every dataset and model size tested, Lambda’s NVIDIA HGX B200 outperforms the NVIDIA 8×H200 NVL substantially. The headline story is latency, not throughput: the NVIDIA HGX B200’s architectural advantages show up most clearly as the NVIDIA 8×H200 NVL runs out of headroom under load.

Interactive latency and TTFT (8B, E4a)

At 116 req/s:

- NVIDIA HGX B200 latency 1.05s vs NVIDIA 8×H200 NVL 2.73s → 62% faster. 

- TTFT 0.0357s vs 0.076s → 53% faster.

At 165 req/s: 

- NVIDIA HGX B200 latency 1.39s vs NVIDIA 8×H200 NVL 15.5s → 91% faster. 

- NVIDIA 8×H200 NVL was effectively saturating at this load; the NVIDIA HGX B200 handled it cleanly.

At 320 req/s:

- NVIDIA HGX B200 reached 53,469 wps with 4.48s latency and 0.0807s TTFT. 

- NVIDIA 8×H200 NVL couldn’t sustain this load.

TTFT stays below 0.081s across all tested NVIDIA HGX B200 load levels → sub-100ms first token even at 320 req/s, nearly 2× NVIDIA 8×H200 NVL’s maximum sustainable load at 165 req/s.

Interactive latency and TTFT (70B, E4b)

At 16–20 req/s: 

- NVIDIA HGX B200 latency 3.25–3.45s vs NVIDIA 8×H200 NVL 13.6–21.4s →76–84% faster. 

- NVIDIA 8×H200 NVL TTFT degraded to 0.522s at 20 req/s; NVIDIA HGX B200 held at 0.095s.

At 75 req/s: 

- NVIDIA HGX B200 reached 11,438 wps with 18.865s latency. 

- No NVIDIA 8×H200 NVL comparison → 3.78× the NVIDIA 8×H200 NVL’s maximum tested load for 70B.

NVIDIA HGX B200 TTFT stays below 0.095s vs NVIDIA 8×H200 NVL’s 0.377–0.522s degradation range at the same r loads.

Interactive latency and TTFT (8B, E5a)

At 1.68–2.4 req/s: 

- NVIDIA HGX B200 latency 2.97–3.31s vs NVIDIA 8×H200 NVL 8.76–36.2s → 66–91% faster. 

- The same saturation pattern as E4a: NVIDIA 8×H200 NVL latency collapses at 2.4 req/s (36.2s); NVIDIA HGX B200 holds cleanly at 3.308s.

TTFT stays between 0.988s and 1.02s across all three comparable load levels → consistent and predictable, vs NVIDIA 8×H200 NVL's 2.72–4.59s degradation range.

At 5.6 req/s: NVIDIA HGX B200 reached 2,002 wps with 44s latency and 3.16s TTFT. NVIDIA 8×H200 NVL could not sustain this load.

Batch throughput

- 8B E4a batch: 52,823 wps vs NVIDIA 8×H200 NVL 23,607 wps → +124%.

- 8B E5a batch: 2,220 wps vs NVIDIA 8×H200 NVL 954 wps → +133%.

- 70B E4b batch: 12,040 wps vs NVIDIA 8×H200 NVL 3,351 wps → +259%.

- 70B E5b batch: 350 wps vs NVIDIA 8×H200 NVL 132 wps → +165%.

### Lambda is the first to publish STAC-AI™ LANG6 results for the NVIDIA HGX B200

The comparison baseline is the independently audited NVIDIA 8×H200 NVL result (HPE ProLiant DL380a Gen12, NVIDIA 8×H200 NVLs) [1]. NVIDIA HGX B200 carries 192 GB HBM3e vs NVIDIA 8×H200 NVL’s 141 GB, and 8 TB/s memory bandwidth vs NVIDIA 8×H200 NVL’s 4.8 TB/s. This is a 1.4× memory and 1.7× bandwidth advantage. In these results, that advantage shows up most dramatically in latency and TTFT under load: NVIDIA 8×H200 NVL approaches saturation at loads that NVIDIA HGX B200 handles cleanly, and the gap widens as request volume increases.

### Why an audited result and not just a vendor claim

The financial services industry is, understandably, skeptical of vendor performance claims. Benchmarks run in ideal conditions, on hand-tuned configurations, and are selectively published. A number that hasn't survived independent scrutiny is, at best, a directional signal.

The STAC audit process is designed to address exactly this. STAC benchmarks are conducted by an independent third party, with a methodology co-developed by technologists from leading financial institutions. The audit covers not just the headline numbers but the complete stack under test, hardware, software version, configuration, and verifies that results are reproducible under the stated conditions.

This matters for two reasons. First, it gives procurement and risk teams a defensible basis for infrastructure decisions, the kind of independently verified evidence that survives internal review and vendor scrutiny. Second, it creates a genuine apples-to-apples comparison basis: when Lambda publishes a STAC number, it can be compared directly against any other STAC-audited system, regardless of vendor. That’s the standard FSI risk teams should hold AI infrastructure to.

### References

[1] STAC-AI™ LANG6 audit, HPE ProLiant DL380a Gen12 with NVIDIA 8×H200 NVL, STAC Research (2025). Available to STAC Observer members at docs.stacresearch.com/HPE250907b 

## AUTHORED BY

 Chelsea Lowman, Chuan Li, Jess Nicholson, and Ravali Reddy

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
