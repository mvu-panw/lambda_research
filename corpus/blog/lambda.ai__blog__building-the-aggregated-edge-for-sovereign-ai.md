# Building the Aggregated Edge for Sovereign AI

Source: https://lambda.ai/blog/building-the-aggregated-edge-for-sovereign-ai

Skip to main content

# Building the Aggregated Edge for Sovereign AI

 August 11, 2025

 (Updated on August 20, 2025)

 • 21 min read

In this podcast of Shared Everything, Nicole Hemsoth Prickett from Vast Data speaks with Ken Patchett, VP of Data Center Infrastructure at Lambda, about the evolution of data centers in the age of AI. Ken reflects on his journey from building Microsoft’s first data center as an ironworker in 1988 to leading infrastructure at hyperscalers and now scaling Lambda. He highlights how AI is reshaping the industry: from the challenge of power availability and the shift toward on-site generation, to the rise of sovereign LLMs and the need for adaptable, multi-density data centers at the aggregated edge. Framing this moment as a “second renaissance,” Ken underscores that collaboration across the industry will be essential to meet growing AI workloads while ensuring efficiency, compliance, and scalability.

### Audio Transcript

0:04: Hey, it's Nicole here from Shared Everything, and I'm joined by Ken Patchett, who's VP of Data Center infrastructure at Lambda. 

 0:10: Hey, Ken. 

 0:11: Hello, Nicole. 

 0:11: I'm glad to talk with you today. 

 0:13: You too, you know, Ken, you have one of the most interesting stories when it comes to data center history and culture. 

 0:21: And even though today we're gonna talk about all kinds of things GPU clouds, sovereign LLMs, data strategies and all that stuff, I want to start with your story. 

 0:30: How did you get started? 

 0:31: Well, that's interesting. 

 0:33: In 1988, I was an ironworker. 

 0:36: Working for a company in Seattle that was building the first data center for Microsoft in the Candid Park facility of Bothel, Washington. 

 0:44: And a funny story is 10 years later I was back running and, and managing that space. 

 0:49: So, from, from an ironworker, I, I moved into working for Compaq Computer Corporation, rebuilding servers in the middle of the night. 

 0:58: And then moved into working for Microsoft, and then from Microsoft, I ended up at Google and Oracle and Amazon, and I've been through the beginning of hyperscale all the way through now. 

 1:09: I remember in the year 2000 sitting on a building with an Iridium phone, a radio, and in a lawn chair in a blanket, of course, because I'm in Seattle and I'm. 

 1:17: On top of this building waiting for something to happen and nothing really happened. 

 1:22: The good news though, nothing. 

 1:23: I, I didn't know how to use the Iridium phone anyway, so I'm pretty happy that that that that happened. 

 1:27: Well, it was interesting because as I look back on, on, on this now, you know, almost 30 years later, it, it is striking to me how I, I was sitting through the advent of, of, of the beginning of this age and this age of hyperscale, and I, I had no idea, you know, where I was at, what I was doing, or what I was going to witness over the next 25 years. 

 1:49: And frankly, it's, it's been pretty amazing and pretty interesting. 

 1:52: I wish I would have kept better notes. 

 1:54: So, during, during that long transition period in large scale infrastructure, you were really on the facility side, right? 

 2:01: So you were thinking about pipes and, and the building itself much more than you were feeds and speed. 

 2:07: Well, I, I would actually say it was all of that because as a data center operations person, you're responsible to make sure your facility is up and running and, and managed at all times, but you also do the server break fix work. 

 2:19: And, you know, I ran networking for MSN for a long time, so I've been on the facility, the network, and the server side throughout my career. 

 2:30: And in fact, the important thing to understand is that a data center technician in large part is a jack of all trades. 

 2:37: And you really end up learning end to end that that the cloud is actually a whole lot of work with really physical components in every way. 

 2:48: So yeah, I've been on, on feeds and feeds and the pipework and pouring concrete and putting in the iron and the steel. 

 2:55: So it's been, from construction management all the way through, making sure that, you know, the millions of customers that are using your platform have access to it. 

 3:03: It's it's been quite a career. 

 3:05: Yeah, I, I would say so. 

 3:06: Leading up to now, when, when we have data centers being built that literally boggle the imagination, where we have to start getting very creative about things that maybe in the early days for you were, well, OK, we have power from the grid here and that's gonna be enough, and we have These contracts and we know that this will all work. 

 3:22: I think there's a conversation to be had about power, and I'll bet you have some unique perspectives there. 

 3:29: Yeah, interesting. 

 3:30: Power is definitely on the top of mind for everybody today. 

 3:33: It is true that infrastructure requires power and it is true. 

 3:37: That the more we move into the super intelligence world that data centers are going to consume an awful lot of power. 

 3:47: And I think there's a misnomer that's really in the industry that says there's not enough power. 

 3:53: There's enough power. 

 3:54: It's just not in the place that you want it, or it's not in the way that you can actually get it or receive it. 

 3:59: And then when you Think about being connected to the grid, the grid also has to be able to manage like this ever-changing workload that we're now seeing with artificial intelligence. 

 4:09: You see power go up and down in large chunks of megawatts where previously it would slowly move 1 or 2% in the course of a week or two. 

 4:19: What we're really finding is that it's really important. 

 4:23: Now to start thinking about your impact on the grid and the fact that John Q Public uses that grid as well. 

 4:30: You're seeing a lot of data center providers start doing things such as on-site power generation in many different ways. 

 4:36: There's lots of, of, of work today going related to natural gas, a battery, battery backup systems, the solar and wind connectivity. 

 4:45: And I see our industry being really, really responsive to the fact that we have to be sensitive with the power and the utilization that we're, we're taking and how we actually impact the grid and the rest of humanity basically that uses the same grid. 

 5:00: And to get to yes, to be able to build the data center in the area that you need to based on the users that you're, you're serving. 

 5:08: I think it's really important to think about on-site power generation as we move forward, and that's becoming more and more of the trend in the industry right now simply because of the advent of artificial intelligence and and what it brings to the table as far as needs for resources. 

 5:23: When, when you first heard about the Stargate system, And with its, it's multiple sources of power. 

 5:30: What's your first thought from the facilities and, and data center standpoint and all the experience that you have seeing the big picture of this, was your first thought power or was it something else? 

 5:39: I, I wouldn't say it was the first thought was power. 

 5:42: the first thought was, wow, that's a lot of construction people in the same place for a really long time. 

 5:46: I, I hope that they can get enough of them there. 

 5:49: Yeah, you know, this notion of being able to bring your own power to a site, it, it really isn't new. 

 5:56: If you think about, let's Say the oil fields. 

 5:58: They've been doing on-site power generation for 25 and 30 years. 

 6:01: It's not a new concept, but it is a new concept in, in the world of data centers in that we just hit that tipping point where it's necessary, and it's, it's, it, it's something that needs to be done. 

 6:12: And so to be honest with you, with you, when I first heard about it, it was like, yeah, of course, they should be tying all these different sources of power together. 

 6:21: You know, you think about transforming industries, it's this kind of thing that does transform the industry. 

 6:27: Our industry has been innovating, which to me means squeezing the same water from the same sponge, you know, until the last drop gets out. 

 6:34: But now we have to transform. 

 6:35: I mean, you're, you're talking about data centers now that that are possibly being run by hydrogen. 

 6:41: And wow, what an interesting concept. 

 6:43: So we're moving off just utility, we're moving off using that system to helping to create the power sources that might feed into the utility. 

 6:52: We're looking at all kinds of new power sources, power generations. 

 6:56: We're seeing Batteries really change the dynamics. 

 6:59: So, I think about hydrogen, natural gas, wind, solar, and all of the things that have to come into existence now for us to begin using all those things together. 

 7:09: And this is a whole brand new world that it is transforming. 

 7:13: I tend to talk about this super intelligence age as the second renaissance. 

 7:18: We're thinking in new ways, we're thinking about new things that we've never had to think about before, and we're pushing the edge, and it's not just power. 

 7:25: I mean, you should Really think about how sovereign LLMs are becoming a thing where the data from countries and how it's been treated is going to change because large language learning models require access to more and more data all of the time. 

 7:39: So there's, there's a huge change and it's completely transforming our industry. 

 7:43: And, and we, we are definitely gonna spend some time talking about cyber LLMs. 

 7:47: Just, just one more question on this, on this more data center centric piece here because I just think you've got great perspective on it and your role there at Lambda and, and it Might be helpful, by the way, give us a sense of first, what the scale is of what land is built. 

 8:00: I mean, you, you are managing quite a bit in terms of infrastructure. 

 8:04: Give us a sense of what you've built there and where you see the challenges being both from a, a more physical infrastructure standpoint and also from a softer and software perspective. 

 8:16: Like, where does this all get really hairy and is it in some unexpected places, maybe? 

 8:21: Yeah. 

 8:22: So great question. 

 8:23: So, so Lambda has a footprint. 

 8:26: Of in the several 100 megawatts where we're an emerging hyperscalar and, and we're really working on being an emerged hyperscalar. 

 8:34: We have data centers in 7 regions around the United States and we're focused right now in the US because it, it really is ground zero for the things that are occurring in our industry as we Start creating the products on what these amazing GPUs can, can, and help us create. 

 8:52: The interesting thing about it is from a data center standpoint is the technology that we use changes every 6 months, and yet data centers take about 5 years from the time you think, oh, I should build a data center over here. 

 9:06: You have to do land, land use, land acquisition, land entitlement, power acquisition, power purchase agreements, interconnects, all this work needs to happen to entitle this land, and then, and then you gotta think about like water, local laws, and it takes a long time to get there. 

 9:22: And once you're there, then you're building this data center. 

 9:25: And so from the time you put your construction set of drawings together and you get permits, it might take you about 2 to 3 years to get that data center ready to operate. 

 9:37: Well, in that time, we've had 4 or 5 iterations of hardware. 

 9:40: So now you have to be really good at building a data center that matches the density of the hardware that's being created. 

 9:47: And so, the data centers of old, we innovated in those data centers from 2 kilowatts a rack to 44 kilowatts a rack, just by changing the way air moves or augmenting it with crack or crawl units or adding a little, changing the water temperature on our chilled water systems, that ended in, in about 2024 because the density of the hardware that's being created lends itself now to rats that are 75, 130, 230 and 1 megawatt racks that we're talking about today. 

 10:22: Those data centers that we were able to tweak for the last 25 or 30 years, we can't tweak those any longer. 

 10:29: This is a net new data center that's actually necessary in order to support this type of hardware. 

 10:35: And with the changing hardware DNA every 6 months. 

 10:39: The data center DNA takes a little bit longer to change, so you have to have a lot of foresight and start building data centers in ways that they can be more adaptable to the fact that maybe some new technological advancement's gonna happen that either increases or decreases the density of, of, of your space and your data center has to be able to support that. 

 11:00: I think about things such as cubic feet per minute in air. 

 11:04: Some racks were, let's say 2500 cubic feet per minute. 

 11:07: Some were 4500 cubic feet per minute. 

 11:09: So if you build your data center wrong, you have a 2500 cubic feet per minute rack, you put 1000 of them in there, you have a deficit in air and all you're ready. 

 11:18: Once you get your data center done, you are redoing it. 

 11:20: There's a huge intensive capital outlay that occurs, so I think it's really. 

 11:25: It's important to understand that we have to build in such a way that we can adapt to the changing technology of the hardware that we're putting into our data centers. 

 11:35: That's, that's one of the biggest problems that we're seeing in the industry right now. 

 11:38: And that being said, it's data center space and availability. 

 11:42: You could have the best ideas, you could have the best product, but if you don't have a data center to put it in, You're not gonna see the light of day. 

 11:50: Time to markets really, really fast, right, are really important for anybody in, in the business world of artificial intelligence or delivering a platform as a service or these enterprise players that are creating products on these large LLMs. 

 12:05: If they can't get it to market quickly because data center space is not available, they may miss that opportunity. 

 12:13: So there's A lot of connected dots here that have to come together and it ranges all the way from delivering platform from the software and managing and monitoring standpoint to digging a hole in the ground. 

 12:25: It's, it's the whole end to end that is being rethunk as it is. 

 12:30: When you think about future proofing, the kind of facilities data center side of is one thing. 

 12:35: Where in the stack do you think there is the most Opportunity to at least start futureproofing. 

 12:41: I mean, you've got the Nvidia GPUs there at Lada, you have, you know, the processors are almost the easy part right now, as long as you can get them, of course, and cool them, you know, where else are you looking at as the key to whatever scalability you're gonna need, whatever efficiency you're gonna need, you know, where, where does this begin and, or is it, is it kind of everywhere? 

 13:03: You know, I think we could divide this into two things here. 

 13:06: You, you have your data center infrastructure space, which is, is so critical to have. 

 13:12: But then when you think about the delivery of a platform and you think about what artificial intelligence really is, you have LLMs, you have inference and other re enterprise workloads. 

 13:23: And when you deploy these in large footprints in singular places, there's a lot of data protection that comes into play now because data needs to be stored somewhere and it needs to be near these large language learning models. 

 13:38: They're hungry and hungry for data. 

 13:40: So when we talk about the efficiencies that we need to plan for, or the things that we don't know, how do we plan for the unknowns, I am increasingly concerned about data privacy laws and the, the creation of regulations that, that force like sovereign LLMs to be created. 

 14:01: And, and what I, what I mean by that is sovereign LLMs are, are rapidly emerging. 

 14:07: They're, they're a strategic priority for governments that are worldwide. 

 14:11: And they look at these models that are designed and they're trained and they're hosted, but they want them to be within their national borders to ensure data sovereignty for their citizens. 

 14:20: These models that we're making, they're, they're designed and they're trained and they're hosted, but now they need to be hosted within national borders, and they, they want to ensure their data sovereignty, their regulatory compliance, or cultural relevance. 

 14:32: And when you think about a large language learning model, taking in data from everybody around the world in order To provide the promise of technology to everybody in the globe, you have to take into consideration that each country and each space does have their own compliance, their own data, and their own cultural relevance. 

 14:49: So the global landscape that we're seeing now, we're witnessing a fragmentation of the AI ecosystems. 

 14:54: They're going into regional blocks, and each of these regional blocks, like, like sovereign LLMs, they're pursuing like localized innovation. 

 15:02: We have to have local regulatory alignment and technological independence. 

 15:06: So I think what you can see is, or what we're going to see and have to plan for, is stricter artificial intelligence uses laws that are tailored to the local norms of the country that you're in and the political systems. 

 15:19: So this is going to give rise to the need not only for some really innovative software work, but also for the new facilities that are going to be able, that are needed to support this. 

 15:28: So there will be new types of data centers. 

 15:31: Built that are in alignment with the of the fact that the workloads that are occurring within a region or maybe a sub LLM, and they're doing enterprise and inference workload and the data is going to be kept locally. 

 15:45: So you're gonna see these super hyper scale data centers that are built, right, for really dense workloads, and then you're gonna see this big area for storage. 

 15:53: There's gonna be a lot of data storage that are going to stay within the local regions. 

 15:58: And that, that I think really causes both sides of this house, the infrastructure side and then the platform software side, to really start thinking about how we're building our products and those products have to mate together to support what is very likely gonna be the most important. 

 16:16: Change in our industry right now, and that's the advent of sovereign LLMs. 

 16:20: The things that are at the top of my to do list related to data center infrastructure with Lambda is to make sure that we plan for our data center deployment such that we can take advantage of. 

 16:32: The capabilities of our platform in all the countries around the world that are very likely going to begin implementing new laws related to data privacy, data integrity, and how large language learning models and the data that they consume work. 

 16:49: So, from an infrastructure standpoint, I, I have this concept of aggregated edge. 

 16:54: We have large language learning models that might have stripped down or anonymized data, and they deliver. 

 17:01: That, that information to the aggregated edge data centers. 

 17:06: And when you think about like what is an, an aggregated edge, it, I'm referring to like a distributed network of regionally deployed, mid-scale style data centers, maybe 50 megawatts or so, but they're located in region, in secondary and tertiary regions that are within a country. 

 17:26: They have favorable network confluence. 

 17:28: There's a lot of fiber diversity and latency performance, but they're not considered tier one data center markets. 

 17:34: And, and so that's where your large language learning model will be. 

 17:37: But these aggregated ed sites, they're strategically going to be designed to support sovereign LLM inference and enterprise workloads and regulated data processing under whatever national jurisdiction that we're in. 

 17:50: So, I'm, I'm seeing these facilities able to aggregate the regional demand. 

 17:55: They provide AI specific services that are closer to the point of generation. 

 18:00: And they create a privacy aligned, latency optimized bridge between the local users and the national or the really, really big international large language model training hubs. 

 18:13: So, I'm seeing a world we're planning for a world where I'm going to have a large amount of geographically distributed buildings that we are calling the aggregated edge because that is where the work is being created. 

 18:28: That's the point of data generation. 

 18:31: And if we have those buildings able to do, let's say 80% of the workload, then we're able to easily comply to any national laws related to the use of AI. 

 18:42: And so it's pretty important for us to get this one right, because data centers are very, very expensive to make. 

 18:48: So in that aggregated edge data center world that you've unpacked for us, and that's a fascinating concept, what are some of the infrastructure? 

 18:57: inside the data center that are absolutely critical to get right in advance so that you have the ability not just to support the regulations that are coming and just the workload demands of, of on-site LLMs. 

 19:11: What do you need to make that happen? 

 19:13: That that's really great. 

 19:14: So I, I should start with something, that, that's really important to understand in the data center world. 

 19:19: The advent of the high density data centers that We see that are necessary for large language learning models doesn't actually preclude the need to have the normal standard air-cooled data centers that we already have and already have in play. 

 19:37: This is in addition to. 

 19:39: So what's really interesting is I see a lot of the industry pivoting to 100%. 

 19:45: High density, high power, AI workloads. 

 19:50: I think what's really important to understand is right next to those racks that are gonna pull 130, 230, or 1 megawatt each, you have to have a large deployment. 

 20:00: Of storage, and storage in general is still the old school data center air cooled, maybe 35, 40, 50 kilowatts per rack, and they need to sit quite adjacent to these large language learning models. 

 20:14: So I see these aggregated edge data centers being hybrid-style data centers with Multiple different density zones that run from 16 kilowatts per rack up to 1 megawatt per rack, and we have to run that all together locally. 

 20:33: So, whereas the data center would normally have a one type of density. 

 20:39: We're gonna have 2 or 3 or 4 types of density and differences on every floor or on every section or every quadrant, and I, I envisioned this world and we all hate to build up in the data center space, but I envisioned this world of 4 floors with a, a big fireman's pole that's running right down the middle of it to, to run all your connectivity, but each floor is different density. 

 21:01: Some is liquid to chip and it's density X or Y, and then some is air and it's density X or Y or maybe one of these floors is strictly left for the infrastructure storage of data and that data storage is only gonna get bigger and bigger and bigger. 

 21:18: I think it's really important to understand that the aggregated edge data centers will be multi-density data. 

 21:23: Centers and we've got to learn how to build those in such a way that it's usable and able to adjust according to new technology that's coming out, but still maintain the environment that all of the equipment that's going to be put in their needs. 

 21:38: It's gonna be a difficult but a really, really fun problem to solve. 

 21:41: And, and so we, we're thinking two things here. 

 21:43: This aggregated edge concept, that's new. 

 21:46: This multi-density data center is not really a new concept, but it really hasn't been done in, in a way that supports the new AI infrastructure. 

 21:54: And then let's layer on the sovereign ELM and the laws that we have to conform to from our platform standpoint. 

 22:01: And we've got quite a job in front of us, so that's what keeps us up at night. 

 22:04: That's what keeps us thinking about how do we do this in the best way that we can most serve the customers that are going to enjoy the benefits of. 

 22:15: The creation of this large language learning model and inference clouds, it's just, oh my gosh, it, it's, again, it's a new renaissance. 

 22:22: These are things that we never had to think about. 

 22:24: You know, as you were describing that, I, I was visualizing it, and it was one of those moments and, and you hear about things like this once in a while, and you, you say, why haven't we always been doing that? 

 22:34: Why would we think that AI data centers have to be these monolithic beasts consuming as much as possible, when in fact, workloads can be variable and, and you do kind of need, you need that agile efficiency, right? 

 22:47: I think that's what you're describing. 

 22:49: Well, it's interesting. 

 22:49: I, I, I think about this a lot, and these concepts that we're discussing aren't really new. 

 22:54: Many people in this industry, we've been talking about these things and thinking about these things, but the business need really wasn't there to drive it. 

 23:02: And as you know, in, especially in, in the technology world, you get so much coming at you at a time, you have to almost be in firefighting mode and it's really, really hard to think forward. 

 23:13: We're always thinking forward, we're always doing that, but now necessity is, is raising its head, and that necessity is causing us all to take these ideas, these thoughts, these concepts that we've all talked about in the conferences and as we're friends drinking coffee at at any great coffee shop in you. 

 23:31: These concepts have been discussed, but now we have To implement them. 

 23:35: Now, the business drivers are such that this is exactly what we need to do. 

 23:39: And the good news is we have an industry full of veterans that have seen these kinds of things and, and have been preparing for them coming. 

 23:46: But once they get here, like everything, everything that you plan goes away the minute you start running it. 

 23:52: But we've had these conversations, we've had these thoughts. 

 23:55: And I think it's time for us all to come together and start moving forward here because necessity is actually raising, raising its head. 

 24:02: The bar is actually now well known. 

 24:05: It's well understood, and I think we're seeing a lot of companies come to work together to make this happen. 

 24:10: I think it's important to point something out here at this point. 

 24:13: The most important thing we can do. 

 24:16: Related to infrastructure is work together. 

 24:20: Many, many companies are starting to work together. 

 24:22: Rising tide floats all boats. 

 24:24: The things that we are doing now as we shepherd in this age of super intelligence are things that are going to impact humanity for a very, very long time. 

 24:34: This is not the time for us to argue, fight, and keep secrets related to infrastructure. 

 24:38: We need to get this infrastructure deployed so that everybody in the world can take advantage of the. 

 24:43: of this technology. 

 24:44: So I am really excited about where our industry is. 

 24:47: I am really excited about where the future is, and this idea of aggregated edge and multi-density data centers and sovereign LLMs, it's not necessarily new, but it's never been, it's never been required for us to stitch it together in such a way as to deliver an end to end product. 

 25:06: And I see storage companies, hardware companies, generator companies, battery companies, software companies all coming together to create these platforms. 

 25:17: Huge change coming in the infrastructure of the past. 

 25:21: And now we're all working together to create this new one and that is pretty compelling argument for us to all keep working together like we have been historically. 

 25:30: And now I think that, that, that connection that we all have together in this industry to deliver infrastructure. 

 25:36: We're all tying around one thing, the world is waiting for us to do it. 

 25:41: OK, and that was an excellent reminder of not just how we're all already working together, but why that needs to continue in the future. 

 25:47: Thank you so much for all of your insights and bringing all the experience that you have to bear on to shared everything. 

 25:53: I appreciate the conversation. 

 25:55: Thanks, Nicole. 

 25:56: I'm so happy to have been here and I'm, I'm really looking forward to working with everybody more as we move into the future. 

 26:02: Great. 

 26:03: Thanks everybody for listening. 

Build your AI factory today!

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
