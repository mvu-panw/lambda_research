# StyleGAN 3

Source: https://lambda.ai/blog/stylegan-3

Skip to main content

# StyleGAN 3

 November 29, 2021

 (Updated on April 4, 2023)

 • 11 min read

### Key points

- StyleGAN3 generates state of the art results for un-aligned datasets and looks much more natural in motion

- Use of fourier features, filtering, 1x1 convolution kernels and other modifications make the generator equivariant to translation and rotation

- Training is largely the same as the previous StyleGAN2 ADA work

- A new unaligned version of the FFHQ dataset showcases the abilities of the new model

- The largest model (1024x1024) takes just over 8 days to train on 8xV100 server (at an approximate cost of $2391 on Lambda GPU cloud).

- We release a 1024x1024 StyleGAN3 model trained on the Wikiart dataset which achieves and FID of 8.1

 Sign up for Lambda GPU Cloud

The StyleGAN neural network architecture has long been considered the cutting edge in terms of artificial image generation, in particular for generating photo-realistic images of faces. Now researchers from NVIDIA and Aalto University have released the latest upgrade, StyleGAN 3, removing a major flaw of current generative models and opening up new possibilities for their use in video and animation.

## The "texture sticking" problem

For those who have spent much time looking at video generated using previous version of StyleGAN, one of the most unnatural visual flaws was the way that texture like hair or wrinkles would appear stuck to the screen, and not move naturally with the rest of the object. See this video comparing StyleGAN2 and StyleGAN3, notice how beards and hair in particular seem to be stuck to the screen rather than the face.

Karras et al. suggest that the root cause of this problem is the StyleGAN Generator making use of unintended positional information which is present. It then uses these as a basis for generating textures, rather than the objects to which they should be "attached". By removing this positional information they hoped that textures would move properly with the generated object rather than with the pixel locations.

To eliminate all sources of positional information requires a thorough analysis of all parts of StyleGAN's architecture. Technically this ensures that the network is translationally equivariant, even for sub-pixel translations[1]. Once all this unwanted positional information has been eliminated the network can no-longer make use of the pixel grid as a reference system, so must create its own based on the positions of generated objects in the scene. This means that textures move naturally during videos and gives a quite striking effect.

## Making it equivariant (the alias-free GAN)

### Architecture

Although the overall architecture stays broadly the same, StyleGAN 3 introduces a number of changes to the building blocks, all motivated by a desire to remove unwanted positional information:

- Replace the constant input tensor with Fourier features[2] and add an affine transformation layer to these features to allow the network to better model un-aligned datasets.

- Remove the injected noise inputs

- Remove skip connections to the output image from intermediate layers and instead introduce an extra normalisation step for the convolutional layers

- Add a margin to the features maps to avoid the leakage of padding information from the boundaries

- Add filtering to up-sampling operations and around the non-linearities to avoid unwanted aliasing. (Filter parameters have to be very strict and are tuned per resolution layer)

- For the "r" config (rotationally equivariant) they use 1x1 convolution kernels (rather than 3x3) throughout the network.[3]

 *Illustration of how some of the intermediate activations of the model (middle) and the output image (right) react to different transforms of the fourier features (left). Although StyleGAN3-T is equivariant to translations the output is severely corrupted under rotations, StyleGAN3-R however is equivariant to both translation and rotation.*

### Datasets

StyleGAN has shown famously good results on the FFHQ dataset of people's faces. Although being challenging for realism, as we humans are so well tuned to recognise a face (and any poor results end up deep in the uncanny valley), images in this dataset are perfectly aligned to ensure that facial features are all located at the same points in the image. To better show off the new capabilites of StyleGAN3 the researchers introduce a new version of this dataset FFHQ-Unaligned, which lets the orientation and position of the faces vary.

### Training

After applying all these changes, training is conducted in largely the same manner as StyleGAN 2, resulting in a network which is slightly computationally more expensive to run. One significant modification is the removal of Perceptual Path Length (PPL) regularisation as this actually penalises translational equivariance which is what they want to achieve.

## Results

So after going to all that trouble to remove any way the network can use absolution positional information in generating images, what do we get out? Well as you can see from the videos, something that looks strikingly more natural in motion than previous models. But of course there is some price to pay, and when it comes to absolute image quality (at least as measured by the standard FID metric) the new StyleGAN3 architecture can't beat that of StyleGAN2 for the original FFHQ (faces) dataset. it does however perform slightly better for data with less strict alignment of FFHQ-U.

The real benefits however, are in motion. Texture sticking has been one of the most noticeable artifacts in GAN generated videos, so finding a way to overcome this with only a marginal cost to overall quality is a big step forward. New measures of these metrics in the paper show that StyleGAN3 significantly outperforms StyleGAN2 in this regard.

The FID quality metric evaluated across different datasets for different models.

## Training your own

So what do you need to train your own StyleGAN 3 model? Well the code has been released on GitHub along with many pre-trained models, of course on top of that you'll need some data and GPUs to run the training.

As the author's point out, the new StyleGAN is slightly more computationally expensive to run given the architecture changes above. They also provide a handy breakdown of the expected memory requirements and example training times on V100 and A100 GPUs at various configurations.

To train the largest models (1024x1024 pixels) from scratch (25 million images) will take about 6 days on 8x A100 GPUs, but in general you won't need to go these efforts. As in many other areas of deep learning, transfer learning is an effective approach for training a new StyleGAN model. Using a high quality starting point (like one of the existing FFHQ models) you can get to reasonable quality results within a few hundred thousand images.

We trained new StyleGAN3-T models on a Wikiart dataset[4] at 1024x1024 transfer learning from the available FFHQ checkpoints. The model was trained on 4xV100 GPUs on Lambda GPU Cloud, we trained for 17.2 million images (which took approximately 12 days) and reached a FID score of 8.11[5].

You can download the Wikiart checkpoint here. We hope this new model will serve as a useful starting points for those who wish to fine tune models as well as providing a rich and diverse latent space to explore.

Although we've used multiple GPUs to expedite the model training, you can also use a single GPU, for example training on the new 1xA6000 instances available in Lambda GPU Cloud takes 208s per thousand images for a 1024x1024 StyleGAN3-T model (this is about 8% faster than a single V100). Smaller models can be trained faster, and thanks to the extra VRAM available in an A6000, a 256x256 StyleGAN3-T model can be trained at 72.7 s/kimg, about 20% faster than 1 V100.

## What next?

Although StyleGAN3 doesn't quite match previous efforts in terms of absolute image quality in some cases, there is an interesting hint at future directions. As previously noted by others[6] scaling up StyleGAN by increasing the number of channels can dramatically improve its generative abilities, the StyleGAN3 paper also shows this improvement for a smaller (256x256) model. Interestingly, there has been little research in simply "scaling up" StyleGAN in terms of numbers of layers as is common with other neural network architectures and it remains to be seen if this is feasible with GANs which are notoriously tricky to train.

One of the striking results from the paper is the demonstration that StyleGAN3 learns very different internal representations to previous StyleGANs. Visualising the outputs of intermediate layers reveals the co-ordinate system across the face that StyleGAN3 must generate itself without any absolute position reference to rely on. A particularly appealing way of seeing this effect is to use the built in visualiser in the StyleGAN3 repo:

After the much anticipated release of the StyleGAN3 code the community immediately started plugging it into their existing tools for StyleGAN2. This was made much easier by the well documented and organised code base, and the high degree of compatibility with previous releases. It didn't take long before people started guiding the outputs of StyleGAN3 with CLIP, with beautiful results demonstrated by Katherine Crowson and a handy notebook by nshepperd, try it yourself here[7]

d i s s o l v e (config-r edition, not a full dissolve) #StyleGAN3 pic.twitter.com/n5Eowm74IP
— Rivers Have Wings (@RiversHaveWings) October 11, 2021

Rinon Gal, one of the authors of StyleGAN-NADA[8] also showed the results of putting the pre-trained StyleGAN3 models into their work. Including the always impressive "Nicholas Cage animal" model:

The Nicolas Cage version of #StyleGAN3-NADA is coming along quite nicely🙃 pic.twitter.com/1RTvnPMuGC
— Rinon Gal (@RinonGal) October 12, 2021

Over the next few months we can expect many more to leverage the new capabitilities introduced in StyleGAN3 in their own work. Both incorporating the learnings of alias free networks into different image generation architectures as well as using StyleGAN3 in the many interesting and novel ways we've seen for previous StyleGANs.

What will the StyleGAN authors turn their attention to next? Well despite the phenomenal success of StyleGAN one notable challenge is in how it deals with complex datasets, and although it can generate extraordinarily high quality faces, it is beaten by other models at complex image generation tasks such as generating samples from Imagenet. In this regard it lags behind well established architectures such as BigGAN and the relatively new method of Denoising Diffusion Probabilistic Models. Will StyleGAN eventually compete with those, or will it tackle new challenges in image generation?

- 

Equivariance in neural networks has recently become a topic of much research. If you're not familiar with the term then take a look at this blog post for a quick introduction. Recent research has revealed that despite assumptions to the contrary CNNs are not translationally equivariant, and many make significant use of this positional information. ↩︎

- 

Encoding spatial information using fourier features have been found to help neural networks better model high frequency details, see: https://bmild.github.io/fourfeat/ ↩︎

- 

Both the use of fourier features as inputs and the use of 1x1 convolutions throughout are similar to previous work "Image Generators with Conditionally-Independent Pixel Synthesis": Anokhin, Ivan, Kirill Demochkin, Taras Khakhulin, Gleb Sterkin, Victor Lempitsky, and Denis Korzhenkov. 2020. arXiv. http://arxiv.org/abs/2011.13775. ↩︎

- 

Wikiart images were downloaded from the Painter by Numbers competition. Small images were discarded and others were resized and cropped to 1024x1024 ↩︎

- 

The 1024x1024 StyleGAN3-t model was trained using gamma=32, horizontal flips, and augmentation, batch size=32. ↩︎

- 

Aydao's "This Anime Does Not Exist" model was trained with doubled feature maps and various other modifications, and the same benefits to photorealism of scaling up StyleGAN feature maps was also noted by l4rz. ↩︎

- 

Much exploration and development of these CLIP guidance methods was done on the very active "art" Discord channel of Eleuther AI. ↩︎

- 

Gal, Rinon, Or Patashnik, Haggai Maron, Gal Chechik, and Daniel Cohen-Or. 2021. “StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators.” arXiv. http://arxiv.org/abs/2108.00946. ↩︎

## AUTHORED BY

 Justin Pinkney

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
