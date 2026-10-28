# ReLearn at CVPR 2026: can AI still learn from humans?

Source: https://lambda.ai/blog/relearn-cvpr-2026

Skip to main content

# ReLearn at CVPR 2026: can AI still learn from humans?

 October 7, 2026

 • 5 min read

AI has advanced fast by scaling models, data, and compute. As foundation models get more capable, an old question is coming back...

What should machines still learn from human intelligence?

That question sat at the center of ReLearn, the CVPR 2026 workshop "Rediscovering Intelligence: Can AI Still Learn from Humans?" that Lambda co-organized and sponsored, with compute credits for every accepted paper. Researchers from computer vision, cognitive science, and embodied AI came together to ask what human intelligence can still teach machines, and where machines should go past the human blueprint.

The invited speakers were Alexei (Alyosha) Efros of UC Berkeley, Manling Li of Northwestern University, Dima Damen of the University of Bristol, Alan Yuille of Johns Hopkins University, Saining Xie of New York University, and William T. Freeman of Massachusetts Institute of Technology. Their talks didn't point to a single recipe for human-inspired AI. Together, they traced a shift in how researchers think about intelligence: from what machines should learn from humans to how machines should represent and experience the physical world.

Three themes stood out.

### 1. When should AI learn from humans?

Efros named the tension in his talk, "When Is It Good to Learn from Humans?" His starting point was provocative: today's AI may already learn too much from us.

At a high level, foundation models distill a huge amount of accumulated human knowledge. Efros called them cultural technologies, systems built on knowledge people have already discovered, organized, and written down.

Human influence shows up lower in the stack, too. Text arrives with a symbolic structure people created, which makes tokenization fairly simple. Vision has no natural vocabulary like that. Even self-supervised visual learning leans on human-designed augmentations that quietly decide which changes should preserve meaning.

So removing labels doesn't remove human assumptions. They move into the representation, the augmentation, or the learning objective.

Human supervision can also expose structure machines still miss. Efros discussed recent work on text-prompted perceptual similarity, where people easily tell apart different senses of "similar": pose, color, texture, or object identity.

That reframes the workshop's central question: where does human knowledge give the right inductive bias, and where should machines find structure on their own?

### 2. Intelligence means representing and experiencing the world

A second theme ran through several talks: building an internal model of the world is harder than seeing it, and how a system experiences the world may shape what it can learn.

Manling Li came at this through cognitive development in "How Foundation Models Build (and Fail to Build) Spatial Minds: A Piagetian View." Drawing on Piaget, she walked through different forms of spatial understanding, from topological relationships to projective and metric representations.

Saining Xie focused on continuous visual experience. People stitch partial views into a coherent picture of the world, remember things they can't currently see, and update their beliefs as things change. His examples showed how hard it still is for models to build global spatial understanding and keep a persistent world state from what they see.

Dima Damen's talk, "Rediscovering Intelligence: Why Egocentric Vision Is Your Best Starting Point," added another angle: the experience intelligence learns from may matter as much as the representation.

Egocentric vision offers a continuous, first-person record of an agent moving through its environment, something internet-scale collections of disconnected images and videos can't provide. Damen connected this to spatial cognition, learning from a single life, and human-object interaction. From a first-person view, objects are things you approach, reach for, pick up, come back to, and watch change because of what you did. Space is felt relative to your own movement. Experience is linked through time, action, and interaction.

That suggests a different model of visual learning.

Could a system learn from the coherent experience of one life, instead of billions of unrelated examples from many people?

Alan Yuille's discussion of SpatialReasoner added explicit 3D representations that connect perception with spatial computation and reasoning. William T. Freeman, presenting work with Eric Li on generative matter models, went a level deeper: before reasoning about objects, how does a visual system decide what counts as a persistent physical thing?

Together, these talks suggest the next stage of visual intelligence may depend on learning persistent, structured representations from continuous interaction with the world, alongside richer image features.

That matters most for physical AI. An embodied agent has to recognize a cup, and also know that it persists, where it sits in 3D space, that it's still there when hidden, how people use it, and how its own actions change the scene.

### 3. Human intelligence as a guide

Taken together, the talks point to a more nuanced role for human intelligence in AI.

- 

Human cognition offers clues about representation: Li's developmental view suggests sophisticated spatial reasoning may rest on structured forms of spatial understanding

- 

Human experience offers clues about learning: Damen's egocentric work shows how rich continuous, first-person, interaction-driven experience is

- 

Human abilities make useful diagnostics: Xie's examples show spatial and world-state skills people handle easily and models still struggle with

- 

Human-inspired research offers clues about physical structure: Yuille and Freeman explore ways to recover the spatial and physical structure behind what a system sees

None of this means AI has to copy human cognition. That's Efros's question again. Human knowledge can be a powerful shortcut. Human development can suggest learning principles. Human experience can show how perception, memory, and action connect. And human assumptions can also limit what machines discover.

The goal may be to find which principles of human intelligence help, and which structures machines should discover on their own.

### From scaling intelligence to structuring it

The last decade showed how far scaling can take learning. ReLearn suggests the next stage may also need deeper thinking about how intelligence is structured.

What counts as an object? How should space be represented? What should a system remember? What can it learn from a continuous lifetime of experience? How should an agent keep beliefs about a world it only partly sees? And which of these structures should come from people, and which should emerge from learning?

These questions get more pressing as AI moves from recognizing and generating content toward reasoning and acting in the physical world.

Lambda co-organized and sponsored ReLearn because this research sits at the intersection of foundation models, world understanding, and physical AI. Working on it takes new ideas about intelligence, and the compute to test them at scale.

Workshop: relearncvpr26.github.io/ReLearn
Workshop organizers: Xi Wang, Yen-Ling Kuo, Tianmin Shu, Asen Nachkov, Alexey Gavryushin, Yan Zhuang, Chuanyang Jin, Jianwen Xie, Luc Van Gool, and Marc Pollefeys

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
