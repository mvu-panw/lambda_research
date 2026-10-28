# From tokens to concepts: how particle models perceive the world

Source: https://lambda.ai/blog/from-tokens-to-concepts-how-particle-models-perceive-the-world

Skip to main content

# From tokens to concepts: how particle models perceive the world

 August 3, 2026

 • 2 min read

Patch-based vision models exhibit a related class of failure modes: fixed patches may split a single object across multiple tokens or place parts of several objects within one token. This, in turn,  makes it difficult for the model to infer object boundaries and correctly associate features across patches—an instance of the broader visual binding problem in computer vision.

To tackle such issues caused by patches, Lambda has actively pursued research in object-centric representations. The transition is simple but elegant: instead of modeling image patches, why not focus on learning self-supervised representations of objects? This approach is called Deep Latent Particles (DLP) modeling, where an intuition of objects is formed in the model's latent space, alongside the position and scale of each object.

Lambda and collaborators have shown that DLPs work well for 2D world models in Latent Particle World Models (Daniel et al., ICLR 2026), where DLPs are trained as world models. But what about 3D? Same issues caused by tokenization in 2D also exist in 3D. There are no object-centric approaches in 3D scene modeling, except for those that already have annotations and synthetic objects. Now, for the first time, Lambda and collaborators have taken the next step in showing DLPs work for 3D scenes as well. In our recent work accepted at ICML 2026, titled "3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning," we extend DLPs to decompose real, colored 3D observations, like RGB-D images and voxel grids into a compact set of interpretable particles, each carrying its own 3D position, size, and appearance.

The work at ICML presents a robust framework for learning 3D object-centric representations. We observed that the keypoint-proposal mechanism that works fine on dense 2D images falls apart on sparse, discontinuous voxel grids. Therefore, we replace it with an appearance-aware K-means prior that clusters in a joint color-and-position space. This is a crucial finding, and in practice it lets particle centers snap naturally to object surfaces and color boundaries rather than empty space. Getting color right is also tricky: without proper regularization, colored-voxel reconstructions collapse toward gray. We addressed this with a dedicated chroma loss.

In our experiments, we show that feeding these 3D particles into a diffusion-based manipulation policy beats baselines that either skip 3D geometry entirely or use dense, memory-heavy voxel inputs without any object structure. This generalizes across 12 MimicGen tasks and 10 language-conditioned RLBench tasks.

Taken together, 3D-DLP is the first self-supervised approach to decompose colored 3D scenes into object-centric particles (without relying on annotations, pre-trained segmentation models, or expensive inverse-rendering pipelines). The learned representations are dense and rich enough to drive robots towards successful task completion. Furthermore, the representations are interpretable, with easy bridges to language and cross-modal information.

Read the full paper: "3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning" 

## AUTHORED BY

 Amir Zadeh

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
