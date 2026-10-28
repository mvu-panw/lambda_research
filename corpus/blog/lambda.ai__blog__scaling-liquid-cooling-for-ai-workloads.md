# Scaling liquid cooling for AI workloads

Source: https://lambda.ai/blog/scaling-liquid-cooling-for-ai-workloads

Skip to main content

# Scaling liquid cooling for AI workloads

 May 21, 2025

 (Updated on August 20, 2025)

 • 39 min read

In this episode of DCD's Keeping It Cool, Emma Brooks of DCD hosts Phil Lawson-Shanks, Chief Innovation Officer at Aligned Data Centres, and Ken Patchett, VP of Data Center at Lambda. Together, they unpack the rapid shift from air cooling to liquid and hybrid systems as AI workloads drive unprecedented power densities. The conversation explores how next-generation chips like NVIDIA’s Blackwell are reshaping cooling requirements, why adaptability and scalability are now critical in data center design, and how operators must rethink infrastructure to support the “intelligence age.” With insights from both the operator and hyperscaler perspectives, the discussion highlights not only the technical challenges but also the transformational opportunities liquid cooling brings to efficiency, sustainability, and the future of AI infrastructure.

Transcript

Hello and welcome back to the Keeping It Cool Liquid broadcast on the data center cooling channel here at DCD. 

I'm Emma Brookes. 

I am head of channels for DCD, and I'm delighted to introduce this episode on scaling liquid cooling for AI workloads, and thank you very much to Aligned Data Centres for partnering with us on this episode. 

So, today I'm delighted to be joined by Phil Lawson Shanks, who is the chief, Chief Innovation officer at Aligned Data Cents, and Ken Patchett, who is the VP for data center architecture at Lambda. 

So thank you very much to you both for joining me today. 

How are you doing, gentlemen? 

No, well, thank you. 

Thanks for having us. 

Thank you. 

Thank you very much for joining me. 

so to start off with, just if I could ask you both for a brief introduction of yourselves, for anyone who doesn't know you, Phil, maybe if I could go to you first. 

Sure. 

So Phil Law and Shanks, I'm at Aligned Data Centres, Chief Innovation Officer. 

I was doing some calculations the other day, and in 2 years, I will have been in this industry for 40 years, which is kind of terrifying. 

But it gives me a perspective of where we've come from, what's changed, and where we're going. 

So, and aligned, we specialize in building scalable building architectures for this technology, for the next technology in the most sustainable way possible. 

 And I'm Ken Patchett. 

I'm the vice president of data and infrastructure for LAMDA. 

I've been in this space for more than 30 years, and I've been fortunate to have a front row seat from the beginning of Hyperscale through now. 

I helped in 1988 to build the first ever Microsoft Data Center in Canyon Park B, Washington as a young ironworker, and I came back to run and manage and operate the data center 10 years later, and then I've been fortunate to work for companies like Microsoft, Google, Facebook, Amazon in the data center hyperscale space. 

   And here we are at Lambda, an emerging hyperscalar, making it happen again. 

   Great, thank you. 

   Well, it's fantastic to have such seasoned experts with me here today. 

   so, to start off with, I want to touch very briefly on some of the drivers towards liquid cooling. 

   yeah, this is of course the keeping it cool liquid broadcast. 

   So I think as an introduction it'd be useful to cover that off just for a couple of minutes. 

   So, Ken, maybe if I can come to you first for the perspective from the chip architecture, you know, I suppose how have recent developments within this, I suppose accelerated moves towards liquid cooling? 

   , it accelerated it for sure. 

   newer chips like, like the Nvidia Blackwell series, you know, they're coming in at 700 to 1000 kilowatts per unit. 

   So, what that really means is the traditional air cooling that we've used in the data center space since Phil and I were in diapers, right? 

   It becomes inefficient. 

   You know, at these levels of density, you just can't do it with air. 

   A traditional data center. 

   Would, would require a tremendous amount of infrastructure upgrades like air volume and velocity to cool at the rack level, densities that we're at now, and the chip proximity to one another is so dense that even the air flow between them isn't feasible. 

   Then, when you think about the workloads that we have, the TDP or thermal power design profiles, they're scratching the capabilities of even the heat seeks that we would have used in the past. 

   So long sustained workloads, higher TDPs that it can be maintained for hours, right? 

   This all necessitates. 

   It all requires a change in the traditional air-cool data centers and we're in the front row of doing that now. 

   Brilliant, thank you. 

   thank you so much, Ken, and Phil, from, from the operator perspective, I mean, how has cooling shifted from, you know, air to hybrid to liquid and how is the line to that in infrastructure? 

   Yeah, that's great. 

   And I wondered what I could add to what Ken was saying there. 

   But yeah, so we, we essentially look at the workload, we look at what's happening in the servers and how we have to build a space to keep those operationally efficient. 

   , and if we look for, you know, we, as Ken said, we've gone from CPUs to GPUs. 

   CPUs behave very differently. 

   they were very much a sequential processing unit. 

   The machines would do their own thing. 

   They would come up and down relative power, across the floor. 

   Now as a GPU cluster, that behaves in a very different fashion. 

   And also, as Ken said, the power density is extraordinary and we've really maxed out. 

   Out on our ability to absorb that heat with air. 

   We've been moving air for a long time, but the business was started and designed to be the most sustainable data center platform, and we adopted a liquid loop inside the building because liquid is the easiest and most efficient way of moving heat. 

   But we'll be using forced air through a technology called the Delta cube to push air across the surface. 

   But once you get to about 60, 60 kilowatts a rack, that's, you're really tapped out. 

   And to get to that point, you know, the servers have to have their fans removed, which I haven't met a customer who's prepared to do that. 

   So we designed for 50 kilowatts a rack. 

   , we're just there. 

   Now we've been doing liquid to the chip for a while with some of our federal clients who are using craze systems. 

   So we take their CDU, we take their liquid to the chip, or liquid to the server. 

   I mean, the whole thing's liquid cooled, and we put that into our loop. 

   So this transition now to this hybridization of the data hall is something that we designed for without really realizing we were designing for it. 

   So now we can just drop in CDU's next to our delta cubes, so our delta flows next to the delta cubes, and we can just push liquid directly into the data hall. 

   Because for the foreseeable future, you'll still need air in those halls as well. 

   Because the, the server systems themselves, the GPU based cluster servers, the majority of that heat, 80 7 80% of that is going to be removed through liquid, but there's still a lot of technology in that machine, as well as all the supporting architecture, the network architectures, the storage arrays, all of those things that still need air. 

   So we're going to have this hybridization for quite a while, and, as I say, we're designed for that without even realizing we were designing for it. 

   Great, thank you. 

   And getting a little bit deeper into some of those design elements that you touched on, you see, there is this certain level of flexibility that's been built into designs now, you know, data centers have to be adaptable, you know, we don't exactly know how dense work is. 

   Clothes are gonna become over the next couple of years. 

   So yeah, Phil, Phil, you mentioned when we talked previously that sort of the focus of the last several years has been about optimizing for the cloud services, see very large LLNs take a different design process. 

   So yeah, you were able to go into a little bit more detail on that approach. 

   Certainly. 

   So we've seen for the last couple of years, as I say, the largest hyperscalers and the emerging hyperscalers I've been designing around creating those LLMs either, for themselves or as a service for others. 

   Now we're getting to that point where they want to monetize that information. 

   So taking those models, and obviously there's still work to be done on those models, a lot of honing and tuning and ratifying the data that's coming out to ensure that it's correct. 

   But now taking those models and pushing them out into the field as an agent, agent AI. 

   So we're now seeing a shift in not only just having large GPU clusters, but also GPU instances adjacent to existing cloud architecture. 

   Because I just put it in very basic terms, for an agent to operate, it needs to have close proximity to a data set and the cloud is the best data set for it to use. 

   So we're going to see this hybridization of existing data centers to accommodate these large GPU clusters, as well as continued large GPU clusters. 

   for the hyper scalers and other people who want to build their own models and tune them and write those agents in situ. 

   So the requirements are going to be liquid and air, as I say, for the foreseeable future, but the scaling is scaling, which is going to be the challenge, but we've got some interesting technologies that we've been developing to accommodate that. 

   Great. 

   And how are you integrating that adaptability into your design processes, yes, as touched on, you know, liquid cooling requirements can change very, very quickly. 

   Yeah, so with, we optimized our data hauls for cloud years ago and we built a provision for adding more of our cooling technology as workloads change, as technology changes. 

   But what we found is that we can within the gaps between our large cooling arrays, our data cube arrays. 

   They're perfectly situated or suited for dropping in CDUs, and the CDUs can attach to the same internal fluid network and then pass the secondary fluid network out to the data hall. 

   So that adaptability was designed from the ground up and then power distribution we can talk about later, but for cooling our standard design accommodates that beautifully. 

   Great, thank you, Phil, and Ken, it'd be good to, to get your perspective on this as well, you know, at the rack level kilowatt per rack is obviously increasing very quickly. 

   you know, data centers are designed to stand for what, 1520 years plus. 

   So, yeah, what, what's your take on some of the design elements that Phil's touched on? 

   Right. 

   I think as we talk further, we're gonna, we're gonna have conversations related to like the elements of data center, you know, you, you, you bring up the, these 20 years depreciating assets and, and it's really interesting because, because when I, when I began in this business, like deploying a 2 megawatt data center across a 30,000 square feet of white space. 

   It was, it was state of the art, you know, 22 megawatts, 2 kilowatt maximum racks, 30,000 square feet, and we are players in the game. 

   But that's not state of the art anymore at all. 

   Like, when you think about this, we advanced to 7.5 megawatt facilities supporting 6.5 kilowatt racks across 35,000 square feet, and that took 15 years to get to, same building, same building. 

   And so we had these meticulous MEP upgrades. 

   We, we did some tweets, you know, we, we, we, we changed the airflow, we changed containment strategies and a, and a host of other like engineering optimizations. 

   But all were like, like, we're, we're talking innovation, not transformation. 

   We took the same box and we augmented it in some way, shape, or form, and we called that like, like different. 

   But at the end of the day, we're, we're now stretching the limits of our existing, you know, infrastructure. 

   You know, Phil uses 50 kilowatts. 

   I'm at about 44 kilowatts. 

   It's about the max that I can. 

   I feel I can safely and consistently cool air cool racks today. 

   From 1996 till now, 2004, we were moving from 2 kilowatts to 44 kilowatts. 

   But you gotta understand the waves of change. 

   Moving so fast now that in the last 2024 to 2025, I went from 4044 to 50 kilowatts. 

   I'm doing 130 kilowatts already. 

   I thought I'd be doing 70, kind of skipped that. 

   Now I'm doing 230 kilowatts. 

   So I think that it's important to understand, we're in a new era, with our current modern chip architectures powering both AI and high performance commute, compute, we have to transform the way the data centers are built today. 

   Think about this, 35,000 square feet and 7.5 megawatts. 

   I can deliver 54 megawatts of IT load in only 9000 square feet of white space now. 

   This really represents an 11,000% increase in power density from, from my 2 kilowatt 35,000 square foot data centers in the past. 

   It is crazy, and that's happened between 2024 and now. 

   The waves of change are going so fast now because we have, we have We're, we're almost entering like a singularity. 

   We're, we're getting to the point where more data, more information, and more, more knowledge is able to be shared more broadly than ever before, that we're moving faster. 

   We're creating things faster. 

   The data center DNA of yesterday cannot keep up with the evolving DNA of technology today. 

   It has to change. 

   Sorry, I get really crazy and passionate about that, but it is, I love it. 

   No, not at all. 

   Well said. 

   And I want to go into a bit more detail on methods to support, as you said, all the changes that we're seeing. 

   So Phil, you've already touched on the importance of scalability, and you know when it comes to design and construction of data centers, obviously rapid deployment and And speed to market is, is, you know, absolutely key. 

   So, you know, how, how is aligned balancing this with the need to adapt to changing customer requirements such as these, you know, liquid cooling requirements that we've already touched on? 

   So yeah, we've, the way we design has really been optimized for this. 

   and as those buildings start changing their locations, I mean, we talk a lot about AI at the edge, and edge, it depends how you define edge. 

   I've always defined edge as the lowest latency point between the service and the consumption of the service. 

   So it's not just in a market. 

   If all the data is actually tromboning through a peering location, it has to be locally serving that marketplace. 

   So to bring AI to the edge requires, is considered an entirely different thought process. 

   But the way, again, we design and say, we've optimized for the ability to scale quickly with traditional compute and now with the ability to drop in those liquid cooling technologies, the CDUs, we can have basically mixed density in the floor, which is going to be critical going forward. 

   We will always have clients like Ken who deploy entirely GPU clusters, but we also have clients that want to deploy one hall is GPU, one hall is cloud. 

   Maybe there's a blend within that same data hall, so we need to have that flexibility. 

   And we can just drop in more and more CDUs and, and go up to 360 kilowatts of cabinet with liquid and air and potentially more as the technology changes, as we, we get better heat exchanges, as we get better distribution of liquids. 

   and there's a whole conversation about how we do that distribution. 

   I think we have so many views on, on flow rates, pipe size, particular count, pressure. 

   , return temps, all of those things. 

   It's going to take us a cycle or two before we have a standardized platform of delivery. 

   But fortunately, the way we've architected our business, we can deploy technology very quickly, build buildings very quickly because of our supply chain, ownership and management. 

   And then we can accommodate those differences, dynamically, regardless of what the client is seeing, or then see maybe in 18 months' time when they take the next set of GPUs from Nvidia or potentially AMD or whomever, and they come back and say, actually, now we need 400 kilowatts of cabinet, we need 600 kilowatts of cabinet. 

-  

   The mindset is entirely viewed on how we can accommodate that in the future. 

   And as Ken said, we built these buildings that have a return on investment for 20 plus years. 

   So our investors are looking for us not to be building obsolete monoliths out in the field. 

   They have to be able to be updated and upgraded. 

   To continue that without any of that depreciation of capital. 

   So many, many things, many forces, but it's what we think about every day in how we design, who we partner with, the way we build, and how we work with our clients like Ken, understanding where they're going and what they need from us, not this year, not next year, maybe the year after that and the year after that, because we're looking for a long term partnership with our clients. 

   Lamb has been a phenomenal partner, and we want to make sure that we're building for them for their foreseeable future. 

   I, if, if, if, if I may, I, I agree wholeheartedly, you know, I, two things, so, you mentioned edge, right? 

   And so, I At lambda, we, we think about, we think about edge is like the extreme edge where data is being generated, right? 

   And then, you know, we have this notion of this aggregated edge where we're gonna have multi-density data centers that as you were describing because there's all kinds of different workloads that are gonna happen and people that use it in France use it in different ways. 

   Some are latency sensitive, some are not. 

   you in our industry, we, we both are getting answers like It depends. 

   It depends on your workload, it depends on what you want to do, and there's such There, there, there's such ability to do so many different things. 

   What I'm seeing, the vision that I think we see here is I, I see 50 or so megawatt buildings being built at what we want to call the aggregated edge where the data that's being generated, it is, is being accumulated and 80% of the workload is happening there. 

   You're gonna see enterprise level doing smaller LLMs at that. 

   Aggregated edge. 

   And so I think there's a, a space where we're going to see multi-level multi-density data centers growing like that at about 50 megawatts because you see, we used to look at the edge, and so as you, you described it, as these lightweight, almost like a a CO, you know, a central office in the old days, but they don't lend themselves to the density that we're seeing today. 

   So I think we're going to see this hybrid of Extreme edge that is really probably going to stick to air cool. 

   There'll be 10 to 50 kilowatts and that's gonna require augmenting, but they're smaller data centers. 

   But all of those data centers, I think about like large, let's say cloud regions, you know, like within the United States, they have all these. 

   Extreme edge spaces and they all aggregate into a place where I have LLLAM dynamic storage and all kinds of other workload capabilities that then serve the local users in that cloud region and then go back to that big gigantic 128,000 GPU LLM in the middle of nowhere, where they need to be right now because of their power density. 

   But what, what's interesting, we talk about like the adaptability and flexibility here, and What we like about working with the line is, is lambda thought processes. 

   We look at data center spaces, there's attributes within every data center and we like to call them elements, right? 

   So a data center isn't just a box, it's got elements such as space, air, water, power, network, and all these detailed attributes of each one of them. 

   So as technology changes, we have to quickly and easily adjust for each of these elements. 

   So instead of building this big monolithic box, we have to build in a more elemental fashion to where I can increase or decrease the water temperature, the air temperature, the pressure, the velocity, the flow. 

   So they've got to be fluid, they've got to be adaptable. 

   That's what I do like about Alliance, by the way, with the delta cube product, it feels like I can move things in and out relatively quickly responding to the ever changing DNA of hardware, which is really hard to keep up with in a data center space. 

   So we're an emerging hyperscalar and we're, we're, we're looking for people to grow with and understand this, and we as an emerging hyperscalar, Lambda has an opportunity to do things in a Different way. 

   So we're working closely with our partners, like Lied and several others, to transform the data center industry. We have to change the way data centers are being built, managed, run, and operated to support tomorrow's workflow. 

   It's changing every 6 months. 

   So, the data center elements have to be able to adapt in the same cadence as the hardware elements that are going within them. 

   How do we do that in a building that we have historically looked at as a 20 year depreciating monolithic asset? 

   That's the kind of work we're doing together right now, and that's the transformation we're trying to dive into our space. 

   And that is exciting. 

   That gets me out of bed every single day. 

   Yes. 

   Oh, me too. 

   Yeah, I think, just to double on that, we've, we've optimized for cloud over the last 5, 10 years, and we can do that really, really well, but the game's changed. 

   So, the density, as you say, Kenny, is changing dramatically. 

   And I think we're just at the beginning of this, and we're very much, and I've said this before, I actually stole this from a partner of Nvidia. 

   We're in an iPhone moment. 

   So back in 2007 when the iPhone came out, that was a very cool device. 

   It blends your MP3 player on your phone. 

   But no one could have anticipated the ecosystem that's developed around having that technology mobile in your pocket all the time. 

   All these businesses have developed and it's how we live now. 

   We're at that point now. 

   It's really, it's almost impossible to predict what's going to come next through the advent of AI and the tools and services that that land is building. 

   We've focused a lot on the, the. 

   , the text elements of, of LLMs. 

   We're getting very rapidly into visuals, into diffusion, and we're running out of, of data to train the models on. 

   So, you know, Nvidia and others and and can and others, they're using artificially generated. 

   data, that's gonna change the world again. 

   And you know, with the Apple Vision Pro, I love that product. 

   It's still waiting for it, it's, you know, it's, it's in full development, but everyone's building those sorts of devices now. 

   So when we get to that point where we can blend reality and augmented reality, we can do, recognition of, of visualization and the agents can then do things with that data. 

   We're going to need so much more processing capacity at the edge and the near edge than we've ever seen before. 

   And again, that requires an entirely different thought process of, of how Ken's going to build his, his infrastructure, how we're going to build, fabric of the buildings to support that infrastructure, and all the modular elements that we need to keep adapting and changing to scale with Ken's workloads. 

   So we're, we're in, probably the most exciting time of our industry that I've ever been in. 

   I, I've been thinking about a closing remark and I am about 100% on board with you right now. 

   This is, this is exactly right. 

   And you know, interesting, the data center is foundational to the promise of what technology is gonna bring. 

   If we can't deploy the data center infrastructure in such a way that tens of thousands of companies around the world can use it and bring the promise of technology to humans, like. 

   Then we haven't done our job. 

   We are the foundation by which all to be built on. 

   I love this iPhone moment thing, because, you know, the issue we're dealing with right now together is simply this. 

   Historically, the facility was the facility. 

   And the IT was the IT. 

   This is one living organism now. 

   These things are not separate. 

   These things are together. 

   I have to manage, monitor, operate and run my IT workload now in conjunction with my facility workload. 

   And this is the first time in the history of us that we have said, hey, facility guy, you're actually an IT guy too. 

   And hey, IT person, you're actually working in the facility, the same monitoring, the same. 

   What do you call this, but the building management systems, for instance, right? 

   They're 10 and 15 minutes to move 1 or 2 degrees, let's say for a still water loop system, right? 

   I have seconds, but I have to monitor the same thing, right? 

   So we're now merging these things into, into a it's, it's an organism. 

   The data center is now not separate from the IT workload. 

   They are, they are. 

   Working together as one organism, one machine, and that is really cool. 

   And, like you were talking about coding and capability to code, we're not software development, is the written word and the spoken word now going forward. 

   In the next year or two, we are gonna see such transformational change simply because we've been able to put this infrastructure together to support the technological changes that are happening in hardware. 

   I've always thought that. 

   That that hardware is the next big thing, and, and here it's becoming true, cause we can We could write software right now to blow up the internet to almost even tie your shoe, you know, but what we really can't, haven't been able to do is get the speeds and feeds to the point where it can really, really manifest, and we're doing it right now, right? 

   And we're in a new renaissance build, right? 

   We, we really are. 

   It's we're entering into, the, the intelligence age and, and we are at the front of that. 

   We're leaving the information age and we're moving into the intelligence age and it's only been, 1945, so 80 years or so, right? 

   So, but, but before that it was 150 years between oh goodness, I, I'm forgetting my, my little age's industrial revolution. 

   The intelligence age now, industrial revolution was before that. 

   And so, we have 300 years or so of that kind of work and then in the last 150 years from the industrial revolution and to the information age was 50 years and now in 75 years, we're out, but it's like we're doubling our speed of transformation. 

   Sorry, I'm getting lost in my thinking here. 

   We really are doubling our speed of transformation from, from the industrial age to the digital age to the information age. 

   It's been 300 years, 150 years now. 

   It's been 80, you know, I'm just gonna use 75 so the math works. 

   No, I agree. 

   I think that together we are the engine of this new age, this new industrial age, and the Renaissance. 

   Exactly, exactly. 

   Yeah, that transition from mechanized to intelligence is extraordinary and it's, it's so, it's fascinating. 

   It's hard to predict where this is going to take us, but we have to do it in partnership because the things you're building, and we all work with, you know, with the GPU and chip manufacturers, and we understand what their, their plans are, you're making it real. 

   And we have to support you, not, as I say, not just for today, tomorrow, but for the next couple of years, because as you do your cycle refreshes, we need to get ahead of that and to be able to accommodate that. 

   And, and you're right, the. 

   The computer isn't just a single instance anymore. 

   It's not even the room scale of these clusters, it's building scale. 

   That's, that's where we're looking. 

   And then it's going to be campus scale as we link those buildings together. 

   it's, it's the most amazing time for us, and I'm, I'm so excited about it. 

   Yeah, absolutely. 

   Well said. 

   Well, unfortunately, I am going to have to move us on just in the interest of time. 

   So I want to talk a little bit about how that efficiency can be optimized as we scale liquid cooling has touched on. 

   So, yeah, maybe if I could jump to you first, Ken, I mean, from your perspective, how does liquid cooling optimize the efficiency of the data center as, you know, workloads get denser as already outlined so beautifully by you and Phil. 

   , you know, that's really, it, it's interesting and, and, and it's, it's actually better, you know, we use power, we consume resources. 

   We have to be really efficient stewards of the resources we're consuming with the work that we're doing, this foundational work, right? 

   So, PUE changes dramatically as we optimize efficiency in the data center with denser workloads. 

   I am ensuring that the electrons that we're consuming and all of the other resources we're consuming are actually moving towards the workload much more instead of just supporting the data center environment that supports the workload. 

   So, for instance, there's A massive drop in cooling overhead right now because of this, new designs that we're seeing, they, they like, like with, with a line, you can drop 90% of of the cooling energy and easily attain PUEs below like 1.1% when you're at the liquid chip scenario. 

   That's a new paradigm, right? 

   That the industry can show a huge efficiency gain in power utilization. 

   So we're now ensuring that the electrons we consume. 

   are dedicated to the workload, as opposed to dedicated to keeping the environment together that these, these, the IT lives in. 

   So we're seeing lower facility overhead, we're better resourced, we're stewards of our resources, right? 

   And frankly, any company like Lambda and any emerging hyperscalar, this kind of thinking about being efficient stewards of resources has got to be built in the DNA of anything that we do. 

   And like working with strong data center builders and providers who also have this DNA, it gives us unconscious competence, right? 

   Because we do business with them, we are participating in the right way to be. 

   Efficient stewards of our resources. 

   So now we can work on things like WUE, like our water usage effectiveness, right? 

   Or our total use of defective. 

   So our carbon usage effectiveness. 

   We're not so stuck on just trying to understand how to better use power and get the value of power, right? 

   Now we're more into how we do these things. 

   So I think total use of effectiveness is probably the next big Focus area that we're gonna be able to look at now that we've solved for let's say PUE. 

   It also saves operational costs that enhances profitability because our electrons that we're consuming are moved to the workload, so it's simply more efficient. 

   And I think that's been needing to happen in our industry for a while. 

   So I think densification is actually really, really a good thing for us. 

   Fantastic. 

   Thank you. 

   And Phil, it'd be good to hear your thoughts on this as well. 

   And maybe some of them hear about some of the technologies that aligns deployed, for example, you know, water saving technologies and yeah, closed loop system designs, which I know you've mentioned previously. 

   Yeah, so we designed closed loop from the very beginning, and we did it really for environmental reasons, but it's, that's brought us to this point where it is the most efficient way of moving heat, frankly, and currently, into the day to, it's single phase, so that's, that's a water loop that's a closed loop that just passes around and and that that liquid passes across every chip. 

   And all the way through. 

   and that's really efficient. 

   We may go to dual phase, in the future, but, but that's going to be driven by, by can and, and, and the GPU manufacturers. 

   That's fine because they'll probably end up being a CDUN row or in the base of the cabinet. 

   We, again, need to remove that heat through these closed loop systems. 

   So everything's, everything's now liquid, regardless of how you're absorbing the heat. 

   The chips themselves. 

   And that goes into the closed loop system as I say, and then we're we're using airside chillers, so we exhaust that into the atmosphere incredibly efficiently and we're constantly looking at ways that we can use that heat, that liquid heat, in other ways, as it takes quite a bit of energy to get, get water up to, you know, 50 degrees C or, you know, 90 °F. 

   It takes less energy to move it beyond that. 

   So to do heat reuse is always a challenge, particularly in the states it's a challenge. 

   We don't have district heating. 

   Typically where it makes sense for us to go data centers, unlike in the Nordics and, and some of the other European countries. 

   But there are other things we can do with that. 

   We're constantly looking at new methodologies, maybe it's greenhouses, maybe it's absorbing liquid from the atmosphere, maybe it's using carbon capture. 

   There's lots of we're constantly looking at those things, but essentially, we've optimized our cooling to, to accommodate the loads. 

   In fact,, as Ken alluded to, with, with those power, you know, incredible cycles that he's seeing. 

   We have to accommodate that with, with, thermal buffering as well. 

   I mean, you can do that with, with the electricity, you know, with the power, you can, you can do mitigation, new capacitors and things. 

   But when you get that spike of heat, we need to absorb that in a, in a fashion so that it gives time for that to be absorbed through the cooling system. 

   So all of these things we're constantly iterating and understanding what's required, but without a closed loop, it's really difficult to scale to these, these. 

   These new densities. 

   There are airside chillers that people will have to deploy in legacy architected data centers. 

   But again, they're going to tap out at a certain kilowatt per square foot ratio. 

   So that's where it's, it's got to be closed loop, going forwards. 

   You know, it, it, it, so for me, it, it won't pencil, I get, as we know, and, and the legacy data center just won't pencil. 

   I think what's important for everybody as we're talking about this is to understand though, we are not talking about building, let's say, machine learning data centers in lieu of the old school data centers that still exist. 

   That is still needed. 

   All of our hyper-skiller friends are still running the same businesses they've been running that require disc. 

   And we're adding this machine learning data center thing to the mix. 

   So it's not. 

   Instead of, it's in addition to that, that we're doing, so we, we have a huge amount of work to do going forward and I really like the idea of like, you know, we have low grade heat, you know, historically with this we are getting higher grade heat, and I think in, in high dense metropolitan areas and there is a really good story for, you know, reusing, heat, you know, some folks showed how they, I can't remember who this was, but, might have been. 

   Might have been another competitor. 

   but, but I think they're, they're, they're heating a swimming pool for the YMCA which normally was like $80,000 a year, and now it's 0. 

   This matters and in areas that we can actually affect Space outside of our data center and our technology bubble, it's really amazing. 

   So I think that lots of new changes are gonna happen, right, that we just haven't been able to do in the past. 

   So anyway, well said. 

   Thank you very much. 

   I'm gonna have to move this forward just in the interest of time. 

   We've got a few minutes left, so I want to address some of these challenges to liquid cooling scalability. 

   So yeah, Phil, I'll come to you first for this one. 

   I mean, what do you think of the different skill sets required from liquid cooling? 

   You know, it is of course different to air cooling, and you know, how can the industry address, you know, the training and these skill gaps that we're seeing? 

   That's a really good question. 

   I mean, we've, we've specialized in training our technicians. 

   We hire smart people, a lot of ex-navy nukes, and we bring them into space. 

   And once you've managed a nuclear submarine, those methods of procedure and the discipline has been fairly, it's a good transition point to running the electrical systems of a data center. 

   Cooling is very, very different. 

   The mechanical aspects of liquid, very, very different skill set. 

   And typically we don't go back into the data halls once we've handed over to our clients, but we're being increasingly requested to be part of that operational structure. 

   So the training elements of how to manage liquid, I mean, once you've, once you've used a particular blend of fluids in a liquid loop, you have to maintain that. 

   You can't change those liquid loops. 

   As new equipment comes in, it's, do you need to purge it, then you need to flood it before you connect it. 

   There's so many different methodologies. 

   So this is, we're still in the beginnings of this, but, we're working very closely with our partners because they've been doing this for a while as well. 

   So together, we need to come together and develop an entirely different set of methods of procedure and standard operating procedures around this, to the point where we may even need to have. 

   Almost like a crash cart with fluid in it, you know, like a big tank so that we can pre, pre-flood the cabinet as it comes in. 

   I mean, these things we're, we're, I wouldn't say we're making up as we go along because we're not, but we're taking best practices from what we've seen in adjacent industries that deal with liquid all the time. 

   And then, and using those skill sets to develop our own teams to to be better stewards of these buildings and, and better service partners with, with, Ken and and, his, yeah, the other, hyper scales. 

   Fantastic, thank you, and, and Ken from, from your perspective, I mean, what are the, do you think are the biggest barriers to scaling, liquid cooling skill sets and otherwise, yeah, and how can, how can these be addressed? 

   I, I, I really feel like I wanna parrot a little bit what, what, what Phil said. 

   But, it's a new space that didn't exist. 

   Like we said earlier, the facility person was the facility person and the IT person was the IT person, right? 

   So now we have monitoring, response time, and support. 

   We're experiencing this fundamental shift in the industry because this is new at scale. 

   I just sleep with the chip thing, but you know what's interesting? 

   It is not new if you're an HPC compute engineer for the last 20 years working in Los Alamos National Laboratory or Oak Ridge or something like that. 

   That's not new for you. 

   If you were a former IBM person, HPC Compute liquid and chip is not a new thing. 

   It is new in the industry at scale, and we're doing it in a way we've never seen it before. 

   And so the IT and facility, like we talked about, share the monitoring in a way they've never done before. 

   They are, they, they've historically been completely separate. 

   They're not. 

   The response times, as we talked about water systems versus IT are completely different. 

   I'm talking seconds versus minutes, right? 

   And so, the skill set that's required here to provide support for liquid cooling running through a rack is not necessarily in the current wheelhouse. 

   Of a hardware support engineer who would typically be troubleshooting memory, CPU and hard drives, right, or the facilities management personnel who are accustomed to saying, I'm not touching that, right? 

   And so all of a sudden we have this, this work that we're all doing together and talking about together is where does ownership of that liquid to chip and what are the new SLAs that we'll ask for? 

   So for instance, Lambda might say. 

   I want you to deliver me a certain amount of pressure and temperature at the inlet of a rat, and I have to promise you the outlet is gonna look like X. 

   But who's supporting the stuff in between the rack right now, right? 

   And then most of the, as Phil mentioned, the stage one, stage 2, you know, from a cooling perspective, oftentimes there is a contamination problem. 

   So a facility wants to stop with their chilled water loop and then you go to the second stage and take it from there. 

   But who's you, the IT guy who replaces hardware? 

   Like, I don't know what to do. 

   There is a gap in this industry right now, and we're trying to figure out as, as a group, how to solve for that. 

   And, and we're doing it as we're moving forward, so contracts are gonna change. 

   The way we work together changes our monitoring, and has normally been completely separated. 

   You can't see mine, I can't see yours. 

   All of that's changing. 

   So that is the barrier to scale. 

   We have to find a new way to work together in a way that integrates our workflows. 

   Absolutely. 

   And, and just to reiterate what you said there, timing is everything. 

   If you had a catastrophic cooling event, like the worst case scenario, some of the cooling failed in an air-based cooling architecture, the temperature's going to rise, but it's going to rise at a predictable rate. 

   And so you've got time. 

   Maybe to switch over to the generator, whatever, whatever it is to mitigate that with liquid, you don't have time. 

   You really don't have time. 

   These chips are designed to run as hot as they possibly can, and they're fairly expensive devices. 

   I mean, I think what I saw recently, the NVL 7200, they, anything from 3.5 to $7 million a rack. 

   And if you lost liquid to a rack. 

   And that's going to break very quickly. 

   So the SLAs are going to be different, very, very different. 

   And as I said, we have to work as a partnership. 

   You know, we share our BMS data. 

   We have secure APIs that deliver that, but we need to increase the frequency. 

   We need to have much more understanding of the workload that's going to be placed upon the room or the building, and so we can accommodate that in, you know, seconds. 

   Yeah, you know, these sorry, Phil, these, I'm thinking that these racks, they're not your old school compact Proliant 5000 scuzzy connected racks, right? 

   You know, me too, they were the greatest, but, but these things are, they're Ferraris, right? 

   You know, they are, they're the biggest, they're the fastest. 

   They're, they're the most critical things that we can do right now, and they're. 

   They require attention, attention like we've never had to give things before. 

   it is. 

   It is so much different than those old school scuzzy rats, right? 

   It's just that it is, it is a whole different world. 

   Yeah. 

   Absolutely. 

   we've got just a few minutes left, so if I could just go to you both, just for a couple of minutes on some final thoughts, and some key takeaways. 

   Ken, if I could come to you first, we've talked a lot about how much the industry has changed over the last couple of years. 

   So I mean. 

   whilst I don't expect to see, expect you to have a crystal ball, you know, how do you see chip development changing liquid cooling requirements over the next couple of years and you know, whilst you've already explained it, you know, maybe in summary, how can we prepare for this? 

   As we, as a general theme throughout our, our conversation has been that the ways of change, they're coming in faster and faster increments than we've ever seen before. 

   We're gonna continue to see densification of chips. 

   But at the same time, I believe we're gonna see an advent of new types of technology. 

   Maybe, maybe some technology will allow us to have chips that run slightly cooler, and we have different space materials. 

   maybe our chips will be able to be spaced further apart. 

   We have different networking materials to allow airflow to go over that work today . We really can't do that. 

   I think there's gonna be. 

   Changes in technology that we haven't actually seen yet to slow this movement towards one megawatt racks, right? 

   That movement is coming because we have to have super dense chips very close together to be able to do the workloads that we're doing. 

   What if there are some Technological changes that do occur, right? 

   And at the same time, we are moving headlong into those one megawatt racks, right? 

   So if, if we're allowed to change some technological activity here that allows us to maybe return to air cooling in some instances, that might be really interesting. 

   So, at the end of the day, Like we said earlier, what we're witnessing and we're participating in right now is, we're changing in age. 

   We're driving into the intelligence age. 

   I believe liquid to chip is the newer and better thing. 

   New networking might help, higher bandwidth, higher chip separation. 

   Many other things are gonna happen, but our industry period is going to continue to. 

   We will continue to iterate, like, like Phil leans into says, well, we're, we're learning, like, and we're iterating and we're moving, we're doing it. 

   So our industry thrives when we build together. 

   Our industry thrives when we work together, right? 

   So the work we're doing here, right, with, with this, it's not just technical. 

   It, it is, it's transformational. 

   I get emotional because we have the power to fundamentally reshape the world right now. 

   And in the data center space, we're fundamental to fulfilling the promise of technology for everyone. 

   We have to deploy intelligent infrastructure everywhere. 

   Lambda believes in a future where every person has access to their own GPS, where compute is ubiquitous for them as electricity around the world, right? 

   So we do say, we're seeing data centers but not as buildings. 

   But it's the bedrock of the intelligence age, right? 

   We're in a new era. 

   One model for every diagnosis and one insight for every heartbeat. 

   It's not innovation, it's, it's a renaissance and it's going to continue to move, and we have to do our job. 

   We have to do it. 

   I love that. 

   And Bill, I'll let you have the last word, if that's OK. 

   Sure, no, I love that. 

   I love that 11 GPU per person. 

   And that's, that's how it's going to be, to have true agents working with us for us. 

   and it's essentially because a lot of people talk about how terrible that's going to be for society, but If you think back to the Greeks, they complained when people started writing things down because for them it was all about the oral translation, tradition of learning, but it accelerated learning. 

   It accelerated the compounding of, of knowledge. 

   And we're at that point now where, having that capability, for all of us to understand things, to, to have access to data that we've never had before. 

   It's extraordinary. 

   It is the most exciting time. 

   It is a renaissance. 

   And, yeah, as a partnership together, we can, we can, we can move this forward because, you know, my view has always been to follow the workload, look at what's going on, what people are trying to do with the technology, make sure we're building the architecture to support that. 

   That cycle is dramatically changing so quickly. 

   That, you know, we're having to think differently, build differently, liquids where it is right now, that, you know, we, we may find better forms of cooling, who knows? 

   But what I can see is that as chips change, there's going to be a circularity process for those chips. 

   Those H100s are being taken, you know, replaced with GB 300s. 

   Those H100s are perfect at the edge. 

   To do some genetic work and then just have this constant cycle of the machines that are running the hardest, most sophisticated compute challenges as they get replaced with the next one. 

   There's still a lot of life in those machines and they're just gonna roll down and we're gonna have distributed compute at a at a scale we've never seen before. 

   I mean, it is the most exciting time. 

   I get very excited about this and we'll have to go and geek out on this somewhere else, Ken and just go and have a cup of coffee and see what we can go build. 

   This works. 

   This works. 

   It really does. 

   Fantastic. 

   Well, what a great note to end on. 

   Unfortunately I am gonna have to wrap it up there because we are out of time, but Phil, Ken, thank you so much for joining me today. 

   It's been really interesting chatting with you. 

   it's been a pleasure and I hope you've enjoyed it. 

   Yeah, as much as I have. 

   Thank you very much. 

   Thank you. 

   Thank you very much. 

   It's a pleasure. 

   Thank you, of course, for partnering with us on this episode. 

   Do of course check for resources out below the episode for some further reaching. 

   Reach out to Phil and Ken if you've got any questions. 

   I'm sure they'd be delighted to hear from you. 

   , this episode will be available on demand shortly, and don't forget, please stick around, for the next episode, in this broadcast at the top of the hour. 

But for now, thank you, of course, to aligned data centers, thank you to Ken and thank you to Bill for joining me. 

Spin up your own liquid cooled NVIDIA HGX B200 today!

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
