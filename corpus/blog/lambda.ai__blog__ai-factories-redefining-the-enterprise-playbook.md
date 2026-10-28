# AI Factories: Redefining the enterprise playbook

Source: https://lambda.ai/blog/ai-factories-redefining-the-enterprise-playbook

Skip to main content

# AI Factories: Redefining the enterprise playbook

 September 30, 2025

 (Updated on November 24, 2025)

 • 17 min read

Yesterday’s data centers were built for servers. Tomorrow’s must be built for GPUs. Lambda is pioneering this shift, reimagining every layer of infrastructure, from power and cooling to network design, to meet the unprecedented demands of AI at scale.

In this theCUBE + NYSE Wired segment from AI Factories: Data Centers of the Future, Kenneth “Ken” Patchett, VP of Data Center Infrastructure at Lambda, joins host Dave Vellante to explore how AI-scale infrastructure is reshaping the data center paradigm.

Lambda's AI factories are engineered for fast deployment, density, and cooling to meet modern AI demands and maximize intelligence produced per watt. Ken contrasts legacy data centers - designed for 2 to 15 kW per rack, with Lambda’s next-generation GPU-dense facilities operating at 130 to 240 kW per rack and beyond, where advances in cooling, metallurgy, and fluid dynamics are redefining what is possible.

He outlines Lambda’s dual offerings:

- 

Public Cloud: on-demand GPU leasing from hours to a year

- 

Private Cloud: dedicated AI factory contracts ranging from about 64 to tens of thousands of GPUs

Both solutions enable enterprises to focus on AI model training instead of the complexities of high-performance compute orchestration.

The conversation reflects on the core theme of AI factories as the new unit of enterprise value. Patchett reframes the idea of “GPU scarcity,” arguing that the real bottleneck lies in the shortage of data centers built for AI-scale workloads. His emphasis on modular, element-based design (power, water, air) and close collaboration across mechanical, electrical, and plumbing systems underscores Lambda’s forward-thinking engineering philosophy.

Looking ahead, Patchett discusses the trajectory toward 128K-GPU clusters, the expansion of liquid cooling at scale, and the potential for on-site power generation and utility partnerships to stabilize power grids as AI deployments increase.

He concludes with Lambda’s larger vision: “one GPU per person”, a call to democratize compute as a force multiplier for human progress, advancing innovation in healthcare, education, and beyond.

### Transcript

Dave Vellante

All right everybody. Welcome back to AI Factories - Data Centers of the Future. We're here high above the options exchange after hours at the NYSC. My name is Dave Vellante and we're here with Kenneth "Ken" Patchett, who's the Vice President of Data Center Infrastructure at Lambda, named of course after our favorite math, lambda calculus for all you function lovers. Ken, thanks for coming on. Great to see you.

Kenneth Patchett

Ah, good to see you, Dave. I'm glad to be here.

Dave Vellante

So we are entering the gigawatt data center in a big way. We're seeing hundreds of billions of dollars and we're going into the trillionaire era, massive build outs. They call you the Superintelligence Cloud. I know you've got a lot of elements to your business that we want to get into, but where are we at in the rise of these specialized clouds? They call them neo clouds. You guys have been supporting developers, you've been supporting model builders. Give us the quick update on your business and your position in the space.

Kenneth Patchett

Well, I like to think about Lambda more as an emerging hyperscaler in that the data centers that we built in the past are still being built and still need to be used, but this newer data center to support artificial intelligence and really these large training models that are being built are very, very special. They're very purpose-built, and the density of hardware is such that the old data centers, meaning 2024 and behind, aren't really suitable any longer for the current deployment of the hardware that we're deploying. So Lambda is in the world of really moving and transforming the data center industry in such a way that we can support these large language learning models, these large training models that are being built around the world.

Dave Vellante

And so when I talk to enterprises, and the particular focus of our program here is enterprise AI, when I talk to enterprises, many of them, in fact, most of them just aren't set up for liquid cooling. Maybe some have mainframes. In the old mainframe days, liquid cooling was a thing, but most enterprises hadn't been thinking about that until the AI heard around the world. So what are you seeing there? Are you saying you are a solution for that? Are you a bridge to that world or a combination?

Kenneth Patchett

I think it's important to understand that Lambda acts as a platform giving access to these GPUs. We believe one GPU, one person in the world. So when you think about the enterprise level player, the enterprise level player will be using the products that are created from these 128,000 GPU clusters that are being built around the world and they'll have enterprise level data center space. So for instance, there'll be smaller data center space with three racks of GB 300, some networking racks and some other types of racks and storage that are there that they leverage and they use. And there'll be multi-density data centers that don't really exist today. Yesterday's data centers were between 2 and 15 kilowatts per rack, and now right next to those racks, we have to put a rack that takes 130 kilowatts or 240 kilowatts. We have to think about how to cool it and things of that sort. So what happens is with Lambda deploying a cloud platform, the enterprise level players are able to leverage the Lambda cloud platform and they don't have to invest their own dollars into that or create their own data center space. We're doing that for them.

Dave Vellante

Okay. So there's a theme. People talk about moving the AI to the data. Enterprises want to apply their proprietary knowledge. They often say, "Well, we don't want to put it in the cloud. It's too expensive," or "We don't want to move the data." At the same time, you guys are providing a service that is unique in demand, not widely available necessarily in traditional clouds. That's how you came to be. How do you see that playing out? Can you accommodate that enterprise? And how do you accommodate that enterprise that wants that propriety, wants that control, but at the same time, needs access to the GPU power and other infrastructure that you have?

Kenneth Patchett

Sure. So Lambda has basically two products that we think about. It's called the private cloud and the public cloud. The public cloud, you can come to the Lambda website and you can say, "I have this much time and this much money and I can lease a GPU for a couple of hours. I can lease a number of GPUs for a week. I can lease them for a year." But it's a public cloud service. On the private cloud, we have the capability for an enterprise level company, for instance, to enter into a contract with Lambda and have access to a large number of GPUs, anywhere from 64 to 20,000 or 30,000 or 40,000 GPUs for elected time. And so Lambda provides the environment by which a machine learning person within any other company can leverage Lambda's GPU cloud and focus on the work that they want to do and not focus on being an HPC compute engineer or worrying about how to orchestrate the GPUs. Our two products there allow you to focus on your job while the platform simply just exists for you.

Dave Vellante

I want to ask you about GPU scarcity, and thank you for that by the way. Sam Altman this week had some very quotable commentary about we can solve education, educating every person on the planet, or we can solve for cancer and we can't do both because we don't have the GPU capacity. Of course, he's projecting sort of forward. How do you think about that? I mean, first of all, is that truly where we're headed in your view as one of the leaders and the visionaries of what's possible with superintelligence or whatever you want to call it, AGI? And are we actually having to make those trade-offs today? I mean, you guys are doing some amazing work in healthcare, in mathematics and all kinds of fields. How are you making those trade-offs today and how are you dealing with that scarcity of compute?

Kenneth Patchett

That's a good question. The scarcity of GPUs, the fact of the matter is the waves of change are happening so fast in our industry right now that it is very difficult to keep up. A data center that has been built in the 1990s isn't suitable to support the GPUs or the hardware that's being built today. If you think about the rate of change, we're getting a new piece of hardware every six to nine months, which changes the requirements to the data center that supports it. So the data centers have to keep up with the changing rate of the hardware. So the way we frame it in Lambda is the data center's DNA has to keep up with the changing DNA of the hardware. And our ability to ensure that we're working with our partners because see, a rising tide floats all boats here. We're working with our partners to forecast into the future what is the right type of data center to build to support the GPUs that are created. Jensen is very clear in nearly every GTC that he's been in, "We've done our job, we have created this amazing product, now you need you to do yours." And what he means by that, or the way we take that is you have to build the data center infrastructure that supports this hardware. So Lambda is working on ways to deploy data centers faster and quicker than ever before. We're thinking about the modularity. We like to think about data centers in terms of elements, whereas as the hardware changes, elements of a data center change, I may need more power, I may need less power, I may need more water, I may need less water, I may need more air. They all have elements to them, and we're working on ways to make sure that the data centers we're building right now future-proof into the future. And so it's really important to understand that the data centers are where these chips are going to go. So when we talk about a scarcity of chips, I think it's better to talk about a scarcity of appropriate data centers to house the very quickly changing requirements of the GPUs that are being created today. The data center space, these AI factories that we talk about are the most important thing to enable not making those choices. Because listen, nobody wants to make a choice about researching for cancer or figuring out how to train every child in the world, like one heartbeat, one diagnosis. That's what we need. We talk about often one student, one teacher. These are not trade-offs that we're making. We're actually using this as a force multiplier for us. A lot of people talk about AI and we think about it differently, like it's happening to us. That's not the way we think about a hammer. A hammer is a tool, and that tool multiplies our effect. So I think about artificial intelligence and the work we're doing as actually a tool that enhances our speed and capability of intellect and thought, and we don't make choices on doing this or that. We are making the choices to multiply our capabilities and actually use that as an enhancement to the human existence.

Dave Vellante

I mean, that aligns with visionaries like Ray Kurzweil who says, "Look, once you get your hands on AI, you're not going to give it back." It makes you smarter. You're not going to want to be dumber. It makes a lot of sense. I want to come back to your one GPU for every human. I called it a chicken in every pot when we were talking off camera. I'm inferring that you are prescribing that the best way to achieve that vision is with the surrounding type of infrastructure, the proper infrastructure that you all are building. Yeah. We'll have GPUs at the edge. We'll have them in our phones. But that vision will be in many respects, notwithstanding the centralized nature of the internet and the world, there will be massive pockets of centralized compute that will serve that vision. Is that the right way to think about it?

Kenneth Patchett

I think it's important to understand that much like the infrastructure that allowed horses to travel across nations and then vehicles following them are the most important thing here. We're building the infrastructure to allow this new superintelligence era to come into play. Let's be clear. 75 years ago, we entered into the Information Age, and in the last 30 to 35 years, it's been the network part of the Information Age, and here are in one lifetime shepherding in two different ages. The Superintelligence Age is what we're fortunate enough to be able to shepherd in. We've lived through scale, we've lived through the creation of infrastructure. Now we're building on top of that infrastructure. So I think what's really important to understand is this. In order to ensure that a GPU and the capability to access it and use it in your everyday life, and to be as ubiquitous as electricity in our existence, it requires infrastructure to do that. Infrastructure takes time, it takes money, it takes intent, and it takes partners. Lambda looks across this industry and our goal is to build the world's largest and greatest platform that many people can use, many companies, tens of thousands of companies can use to create products with. We can't do that alone. We have to do that with folks that know how to bring available power to build the data center spaces to work together for the MEP, the Mechanical, Electrical, and Plumbing pipeline. It takes a large amount of people in our industry to actually deliver the infrastructure that then allows the power of technology to be available to everybody. Lambda thinks about that in a very, very partnering way. We are bringing our partners with us.

Dave Vellante

So I want to ask you about sustainability and liquid cooling. You talk about 128,000 GPU clusters. We're moving toward the era or the holy grail of a million GPU clusters, and we'll go beyond that. You mentioned 2 to 15 kilowatts per rack being now up to 240 kilowatts per rack and rising. Last year at Supercompute in Atlanta, we had a panel on, we had a debate on liquid cooling, and we were debating the single phase versus two phase. We actually had a company on, the name of the company was Omni Services. Nobody had ever heard of Omni Services, but they made hoses and we had this conversation about hoses and connection integrity and down into the bowels basically of the data center and secondary fluid networks and things like that. This is the infrastructure that you're talking about that is hidden. What is the state of that and how important is that? Because if that fails, it's like when the plumbing in your house goes, no cool water, no hot water, you've got troubles. Can you talk to that?

Kenneth Patchett

Yeah. that is the talk of the town. That's the work that we're all doing. Here's the changing times. Supercomputing was really full of hardware and data center personnel this year in Atlanta, wasn't it?

Dave Vellante

It sure was.

Kenneth Patchett

You don't normally see that. But now we are reimagining and reengineering nearly everything because a rack in and of itself now, a rack of compute, a rack of servers used to be a very special thing, and the IT guy takes care of that, and then you've got your facility and your facilities engineers and they take care of that. These are two separate things. Not today. These things are one engine. As we move towards one megawatt rack, how to cool it, how to manage it, how to operate it requires all kinds of PhDs because we have to think about new metallurgy now, we have to think about the difference in materials that we're dealing with, we have to think about difference in liquid and fluid dynamics, air movement, air volume. Everything is going to change, and we're all working together now looking at a data center as a unit of compute now as opposed to two separate things. It's an engine in and of itself, and all of these things are coming together like they've never come in before. You'll hear somebody talk about, "Oh, well, we fixed the liquid to chip problem because we just took the pumps in the water outside of the rack, and we put it over here and made it somebody else's problem. It doesn't really work like that. We are pushing liquid at pressures and temperatures never seen before. So there's a huge amount of work and effort going on, and the cool thing about our industry right now is we're all coming together and we're underneath this problem and looking at this problem of scale, and we're looking at it together. We don't have somebody in the top of the problem and the bottom that are polarizing. We are looking at this problem saying, "Wow, we've got to come together and recreate and reimagine and not just innovate. We have to transform our industry." So you're seeing transformation happen right now like you've never seen before and Lambda is a part of that. We have mechanical electrical engineering people working with the data center space, working with the HPC compute engineers, and we're trying to find the new and best way to deliver this infrastructure technology. If you want to geek out on hardware, this is the place to do it right now.

Dave Vellante

I love it. My colleague, David Floyer and I, earlier this year, we forecast the data center market and we observed, the data center all in has been a couple of hundred billion dollars. It was like a perpetual industry at that level, up and down a little, maybe COVID affected it a little bit, and then all of a sudden it jumped up last year to 350 plus billion dollars, talking the infrastructure, the storage, the compute, the power, et cetera, power and cooling. And we were looking at it and saying, "Wow, this thing is going to continue to grow at massive double-digit CAGRs over the next decade." So we've got it hitting, call it a trillion dollars early next decade. Some people probably have it before that. Probably be half a trillion this year. Just never seen anything like this. I mean, just massive, massive growth. Now, when we put that forecast out there, of course people said to us, "Yeah but what about power? What about energy? That's the big limiting factor." And everybody sort of points to that, and the assumption that we made is that the value that's being created here and the productivity boom that is coming, there may be a little downturn, like there always is in these so-called bubbles. But the assumption that we were making is that the industry to your earlier points is banding together and we'll solve this problem. You've got an administration that's aligned with the industry. You're trying to prove that you can deploy energy. I mean, look what they've done with GPUs, trying to compete with DeepSeek, trying to compete with Nvidia when they were somewhat shackled. So it seems like where there's a will, there's a way for this industry. I wonder if you could address that. Is that overly optimistic? Eric Schmidt says, "Well, maybe superintelligence is going to solve that problem." Others feel like quantum will be, but that's a ways out. What's your take on the blocker of energy? How do we get through that?

Kenneth Patchett

Anytime you experience dramatic change, oftentimes there's an upset or a remixing of the status quo and the way things were. I think we're going to find that in the end of this particular cycle that the data center's growth actually helps to stabilize and create a better overall grid in every country that they're working in. As it sits now, it feels like we're taxing the grid because the grid hasn't had to support this type of demand in the past. But as we start growing together and working together, we're going to find that we're going to get through this particular time, and then we're going to actually see a much more stable grid. A lot of the data centers are starting to do onsite power generation, so every one of us, we do think this way. You have to be the most efficient steward of the resources that you consume. You can't just go willy-nilly and just keep building, building, building and not actually understand how to be efficient and use these resources wisely. And again, a rising tide floats all boats. We have to work with our partners, our government regulatory commissions, all the utilities. They're accustomed to 20 and 30 years of working like this. We're bringing in a new dynamic now into the grid with lots of data centers spread around the world, and as we start working together and get these data centers up, all of a sudden maybe more power will be to the grid or able to be distributed better. I see a world where, yes, it's a little chaotic today, but going forward, as long as we all continue to work forward, work together to create the type of power generation where you need it, we're going to be okay.

It's important to understand there's a lot of power. It's just the power is where you need it. That's not always true.

Dave Vellante

You remind me of the whole art of the possible. I'm reminded of Earl Nightingale in the 1950s, he put out a video, The Strangest Secret. It was an audio actually with his picture. That's state of the art back in the 50s. And one of the lines in there was, "You don't even have to compete. We live in the greatest land in the world. All you do is create." But somehow tech became this zero-sum game and certainly in the 80s and the 90s. But the hyperscalers have shown that you can have three, four, and now with companies like yours more thriving, that it's not a zero-sum game. And the possibilities in the vision that you're laying out, they're enormous. I heard Michael Dell on a podcast. It was on the BG2 Podcast. They were asking him, "Are we over-investing? Is this a bubble?" And he had a great line. He said, "Well, the global GDP is ..." I don't know, 115, $120 trillion. People are talking about 10, 20, 30% productivity impacts. I heard somebody the other day talk about 8X productivity impact for the developers. So he said, "Just do the math." We're spending maybe 3, 400 billion on data center build-outs this year. Call it half a trillion. 10%, that would bring you to 10, 11, 12 trillion. So his premise was we're underspending. Now again, maybe we hit some trough at some point and everybody freaks out, but the long-term vision that you're laying out is of a different world solving problems that were previously unsolvable and driving a productivity boom and potentially a healthcare transformation like we haven't even been able to envision. I'll leave you with final thoughts on that.

Kenneth Patchett

Final thoughts on that really are, when you think about access to technology being a fundamental human right, it's not just about business. We're enhancing the human experience. We're using the technological advancements that we've made, the things that we've unlocked to act as a force multiplier. We're taking our brain and we're making a bigger hammer, like with that or a spoon or another tool to actually bring us forward into this age of intelligence. So to put money on it, it is about moving humanity forward in a way that everything else will follow. If we really truly want to deploy infrastructure, it takes dollars, it takes money, it takes time, it takes intent, it takes cooperation, it takes will, and Lambda wants to create a platform by which tens of thousands of people otherwise wouldn't have access to this type of platform to create tools that enhance the human experience, we want to do that, we want to be a part of that, and I do believe that everybody that I talk to in this industry, and I've been in it more than 25 years from the beginning of hyperscale till now, we've built to this point. So Lambda is really excited to be an emerging hyperscaler to help do that. That is the goal. The goal is to bring technology to the hands of everybody who can use it.

Dave Vellante

Well, you're laying out a really exciting vision, Ken. I appreciate you participating in the NYSE Wired and theCUBE's program on Data Center of the Future and AI Factories. Thank you so much for being here.

Kenneth Patchett

I'm glad to be here and I'm glad to be part of the Intelligence Age.

Dave Vellante

Awesome. All right. Thank you for watching. 

Reserve your AI factory today.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
