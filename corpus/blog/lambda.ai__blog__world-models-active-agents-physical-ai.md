# From world models to active agents: the next step for physical AI

Source: https://lambda.ai/blog/world-models-active-agents-physical-ai

Skip to main content

# From world models to active agents: the next step for physical AI

 October 1, 2026

 (Updated on October 22, 2026)

 • 7 min read

Generative AI has made remarkable progress in creating increasingly realistic representations of the world. Image models can synthesize photorealistic scenes, video models can generate complex dynamics over time, and emerging world models are beginning to capture geometry, motion, and interaction.

But generating the world is not the same as acting in it. An AI system operating in the physical world must do more than predict what might happen next. It needs to recognize what it doesn’t know, decide what information to gather, take actions based on its current understanding, observe the consequences, and continuously adapt its plan.

This shift from passive world modeling to active interaction was the motivation behind the CVPR 2026 Workshop on World Models Meet Active Sensing and Closed-Loop Planning (WMAS).

WMAS brought together researchers from generative modeling, computer vision, robotics, and embodied AI. We co-organized and sponsored the workshop that featured talks from Nicholas Roy of MIT CSAIL, Alan Yuille of Johns Hopkins University, Yiannis Aloimonos of the University of Maryland, and Chelsea Finn of Stanford University and Physical Intelligence, alongside 20 accepted papers exploring world models, active sensing, robotic policies, multimodal control, and evaluation.

At the center of these talks was one question.

How do we move from models that generate the world to agents that can intelligently sense, reason, plan, and act within it?

## World models need more than realistic generation

World models learn representations of environments and how those environments evolve. Given observations and actions, they can model possible future states. But once they become part of an intelligent agent, visual realism alone is not enough.

This gap was particularly visible in RoboWM-Bench. The benchmark evaluates video world models by examining their generated videos, converting generated manipulation behaviors into embodied action sequences, and testing whether those actions can actually complete tasks. Its evaluation reveals a critical gap: videos that appear visually plausible can still produce behaviors that fail under execution because of spatial reasoning errors, unstable contact predictions, or physically inconsistent deformations. In other words, looking right is not the same as being actionable.

This is especially important for physical AI. A robot interacting with an unfamiliar object doesn’t simply need to generate a plausible video of what might happen. It needs representations that preserve the aspects of the scene that matter for action: geometry, object relationships, dynamics, uncertainty, and physical constraints.

GEM-4D approached this problem from the modeling side. The work introduces dense 4D correspondence supervision into a video world model, encouraging it to maintain geometric consistency across generated frames. An inverse-dynamics system then converts these generated rollouts into executable 6-DoF robot trajectories. The authors report that this geometry-grounded approach improves real-world manipulation success from 61% to 81%.

These papers illustrate two sides of the same challenge: one asks whether generated futures are physically executable; the other explores how to make generated futures more geometrically grounded so that they can better support execution. This raises a deeper issue: what a world representation must capture to be useful for decision-making.

The same question was reflected in the invited program. Nicholas Roy's talk, “World Models and Why We Should Care about Their Structure,” placed the structure of world models at the center of the discussion, while Alan Yuille's “World Models: Bayes or Bust?” brought probabilistic reasoning into the conversation.

The emerging goal, then, is a representation of the future that an agent can reason with and act on.

## Intelligence includes knowing what to sense

Before an agent can decide what to do, it needs to understand its own situation in the world. SAW-Bench shows how difficult this remains for today's multimodal foundation models. The benchmark contains 786 real-world egocentric videos and 2,071 human-annotated questions spanning six situated-awareness tasks. Across 24 evaluated models, the authors report a 37.66% gap between humans and the best-performing model.

More importantly, their analysis shows that models can exploit partial geometric cues while still failing to construct coherent observer-centric geometry, leading to systematic spatial reasoning errors. This matters because an embodied agent doesn’t observe the world from an abstract, third-person perspective. It must reason about the world relative to where it is, how it’s moving, and what actions are available to it.

Even understanding the current observation is only part of the problem. Most current AI systems process whatever information they’re given: an image, video, audio stream, or collection of sensor measurements. An active agent can do something fundamentally different. It can actively seek out the information needed to reduce uncertainty.

Imagine a robot attempting to manipulate a partially hidden object. Rather than immediately acting on incomplete information, it might change its camera viewpoint, inspect the object from another angle, or determine that tactile information would be more useful than another visual observation.

Perception therefore becomes part of the decision-making process. Instead of only asking, “What can I understand from what I see?”, an intelligent agent can also ask, “What should I observe next?” This is the central idea behind active sensing: observations are not simply fixed inputs, and the agent can actively seek the right information at the right time.

## Generative models are becoming part of the action loop

Generative models are beginning to move from prediction into action. Yiannis Aloimonos's talk, “Generative Action Systems,” directly reflected this transition. Chelsea Finn's “Evaluating and Improving Robotic Foundation Models with World Models” connected world modeling with another rapidly developing frontier: foundation models for robotic intelligence.

A generative model can imagine possible futures. A world model can represent how actions may change those futures. Active sensing can determine what information to acquire next. A policy can then select an action, and the result becomes a new observation.

Rather than following a traditional open-loop pipeline, these components form a continuous cycle:

Sense → Understand → Predict → Plan → Act → Sense Again.

The three oral papers illustrate different parts of this loop. SAW-Bench highlights the challenge of understanding an agent's situated relationship to the physical world. RoboWM-Bench shows that generating a visually plausible future does not necessarily mean that the implied actions will succeed when executed. GEM-4D demonstrates how incorporating geometric structure into generated futures can help translate predictions into executable robot trajectories

Other work presented at WMAS further explored this connection between generation and action. Imitation Learning Through Imagination in Latent Space explored how imagined trajectories can contribute to policy learning

These works reflect a growing convergence between generative modeling and control. A generated future no longer needs to be the final output of a model. Instead, it can serve as an intermediate representation that helps an agent reason about possible outcomes and decide what to do next.

## From generative AI to physical AI

Generative AI is expanding beyond creation and prediction toward systems that continuously interact with their environments. For physical AI, this shift is fundamental.

The physical world is partially observable and constantly changing. Sensors are imperfect. Objects become occluded. Actions have uncertain consequences. An intelligent agent therefore can't assume that everything it needs to know is contained in its initial observations. Instead, it must keep asking, "What do I know?" and "What do I need to know next?" and "What should I do given what I know now?"

World models, active sensing, and closed-loop planning provide complementary pieces of this problem:

- World models allow an agent to represent the environment and imagine possible futures

- Active sensing allows it to strategically acquire information and reduce uncertainty

- Closed-loop planning allows it to continuously revise its decisions as new observations arrive

Combined, these capabilities move us toward AI systems that do not simply model the physical world, but can explore, reason about, and act within it.

## What’s next

WMAS brought together researchers from generative modeling, computer vision, robotics, and embodied AI around a shared challenge. How do we build models that don't just imagine the world, but intelligently interact with it?

The research presented at the workshop suggests that getting there will require progress across the entire perception-action loop: from situated awareness and structured world representations to active information gathering and predictions that remain valid when translated into physical actions.

Many fundamental questions remain:

- When should an agent gather more information rather than act?

- What should a world model represent for effective planning?

- How should uncertainty influence action?

- How can models adapt when they encounter environments different from those seen during training?

- How should we evaluate systems in which perception, prediction, and action are deeply interconnected?

These questions extend beyond any single area of generative modeling or robotics and point toward a broader goal for physical AI. The next generation of generative models may be defined not only by what they can generate, but by whether they can use their understanding of the world to decide what to sense, how to act, and how to adapt when the world responds.

That’s the transition from world models to active agents and the challenge that will shape physical AI.

Workshop: cvpr26wmas.github.io
Workshop organizers: Rama Chellappa, Jieneng Chen, Yilun Du, Sanjeev Khudanpur, Cheng Peng, Tianmin Shu, Chen Wei, Jianwen Xie, Alan Yuille

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
