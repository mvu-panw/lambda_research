# ShadeRunner: Chrome plugin for enhanced on-page research

Source: https://lambda.ai/blog/shaderunner-chrome-plugin-for-enhanced-on-page-research

Skip to main content

# ShadeRunner: Chrome plugin for enhanced on-page research

 February 13, 2024

 (Updated on February 23, 2024)

 • 4 min read

In today's digital era, accessing information efficiently is crucial. Our new Chrome plugin, ShadeRunner, aims to simplify this process by offering a range of features designed to streamline your browsing experience. This blog post reviews how ShadeRunner maximizes online research efficiency with features including text highlighting, paragraph summarization, and topic suggestions, and provides step-by-step installation and contribution instructions.

## Table of contents

- About

- Features

- Getting started

- License & contributing

## About - improve your online research

How do you know if a Large Language Model (LLM) response is right or wrong? In general, you don't – if an answer matters to us, we need to check the source material. So, how about we make the browsing experience a bit more fun?

Check out what our plugin brings to the table:

- Quick Source Finding: Fly right to the source of a search term like a superhero.

- Colorful Topic Explorer: Highlights related topics in vibrant colors, just like those fifth-grade textbooks, but smarter.

- Dynamic Summarizer: Shrinks down long paragraphs for a quick read. Curious for more while skim-reading? Just click to unfold the full story.

Ready for a sneak peek of these cool features? Just scroll down! And if you're eager to dive right in, check the installation instructions right away. Let's get started!

## Features

### Source Finding

This feature is like "Ctrl + F, but on steroids". Just enter your question or a summary from another source, and find the most relevant sentence on the page in a snap.

#### How does it work?

- First, it processes all sentences on the page, converting them into vectors and storing them in a local database. This happens while you type.

- When you send the request, the plugin also converts your question

- Finally, the plugin identifies the nearest sentence to your question's vector and highlights it. Efficient, precise, and handy.

See it in action below. 

### 
Topic Explorer

Sometimes, the answer isn't straightforward, and you're more in an exploratory mood, right? That's where our Topic Explorer shines!

#### How does it work?

- Like before, it turns all the sentences on the page into vectors. Think of them as unique fingerprints.

- Now, here's the twist: instead of hunting for the closest match to your query, the plugin consults a Large Language Model (LLM) to brainstorm topics related to your input.

- The LLM plays a game of "Hot or Not" with topics. Searching for "engine types"? It'll tag "combustion engine" and "electric engine" as hot (interesting) topics. Cold (uninteresting) ones are things like "general mechanical components", "vehicle brands" or "site navigation".

- The plugin then matches each sentence on the page with the nearest hot topic and highlights them in a burst of colors. It's like watching a firework of insights!

See it in action below.
(Note: Footage sped-up as LLM response may take very long - but the Highlighting is fast).

### Dynamic Summarizer

Ready to dive deep but want to skip the swimming lessons? Our Dynamic Summarizer is your snorkel gear! Why wade through pages when you can get the gist first? This nifty tool is like having a personal assistant who reads all the heavy stuff and gives you the highlights.

Hit the "Summarize Paragraphs" button, and watch as the LLM munches through lengthy texts, turning them into bite-sized summaries. Want the full story? A simple click toggles between the nutshell version and the original text. It's like having a book and its cliff notes side by side!

(Note: The demo footage skips the waiting time for the LLM response. Well, LLMs like to think things through...) 

## Getting started

### Installation instructions

- Download the latest release.

- Unpack the zip file.

- In Chrome go to "Manage Extensions > Load Unpacked" and choose the unpacked folder.

- Activate the plugin.

- Add your openai api-key in the plugin settings.

- (Optional:) Pin shaderunner to your toolbar.

Or, if you want to build From Source yourself:
To create a production build, run the following: (If you want to develop yourself, see below.)

pnpm build
# or
npm run build

Open your browser and load the appropriate development build. For example, if you are developing for the chrome browser, using manifest v3, use: build/chrome-mv3-prod.

## License & contributing

The project is released under the MIT License. Want to make a feature suggestion? Visit our project's GitHub page and submit a pull request. Your contributions are welcome!

## AUTHORED BY

 David Hartmann

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
