Title: Weeknotes 8/31: The Inaugural One
Date: 2024-08-31
Category: Weeknotes
Tags: hardware, Bible, vinyl records

Something I've noticed a lot of bloggers doing is a "weeknotes" kind of thing, where they throw together a brief write up of what they've been learning or interacting with over the course of the week. I'm gravitating toward this idea and I want to give it a try. With family life where it is at this stage, it's just hard to devote the time to sit down and write what feels to me like a large piece. The effect of that is less writing overall. 

But I don't want to let the perfect be the enemy of the good, so I'm going to try to see if I can manage at least a few words, that aren't especially eloquent or organized, about whatever I've been doing lately. Let's give it a shot!

#### Scripture Memory App 📖️

Something I've been doing lately is working on a scripture memory app. I bought Andrew Davis's recent book [How to Memorize Scripture for Life](https://www.crossway.org/books/how-to-memorize-scripture-for-life-tpb/), and became very interested in the simple method he lays out for memorizing massive portions of the Bible.

One of the things this method requires is keeping a journal of all the verses you're learning, and noting how much you've reviewed each verse. But I don't really like journals, and this just sounds like an arduous bit of work that would eventually turn me off from the whole thing. It also sounds like a bit of work that can be automated rather easily.

I think ideally you would want a mobile app for this. I'm not a mobile developer though, I'm a web guy. It was my burden to throw together at least a barebones functional web app that I can stand up on my own machine and use everyday. Each day, it tells me which verses I need to review, and which verses I need to learn. Currently, I'm on track to have hopefully have Ephesians memorized by the end of the year.

Through a remarkable turn of God's providence, it turns out a good friend of mine used to be a member of Andrew Davis's church and knows him well. So it wouldn't be impossible for me to get in touch with him and discuss making this an "official app" for the book, if I wanted to.

I haven't open sourced it yet, only because I might actually try to spin this out into a real app someday. However, I did need to create (yet another? there were a lot of these on PyPI) python library for working with Bible verses, called [pible](https://pypi.org/project/pible/). You can look at that if you like. 🙂️

#### Birds 🐦️

I have a friend who's a self-acknowledged bird nerd. He inivited me to go birding with him a few weeks ago. The migration was already starting, and we live in a good spot to see many species passing through.

It was a lot of fun! I love spending time outdoors in nature, and this just deepened my appreciation of that. Instead of walking out and saying, "Cool! There's a bunch of birds," now I say, "Whoa! Is that an osprey? Let's see if he dives! And what's a pelican doing up here?"

So, I've purchased a set of binoculars: the [Vortex Diamondback HD, 8x42](https://vortexoptics.com/vortex-diamondback-hd-8x42-binoculars.html). This is a great starter set for birding. Vortex offers a great unlimited warranty on all their stuff, so this feels like a great investment.

#### Records 🎚️

These days, vinyl records are my preferred way of experiencing music. I'm an audiophile wanna-be&mdash;I don't have a hi-fi or anything. But I do have a USB turntable, and I have music that I only own on records. So I've had a longstanding item on my project list to rip some records.

The way I've done this in the past is just recording the turntable with Audacity, trimming silence, and splitting up the tracks. However, Audacity just isn't a great tool for this. I really need to listen to the record as it records&mdash;if the needle skips or something, I need to start recording that entire side over again, and one side of a 12" record is something like 22 minutes. If I have a problem in the first two minutes, I'd love to know so I can immediately restart and not wait 20 minutes to find out. 

But turning on input monitoring so you can hear what you're recording in Audacity causes skips and crashes. It did so some ten years ago when I was first doing this. But today, the Linux kernel is real time, I'm running a Ryzen 7 5700G with 16GB of RAM. There's no excuse for this happening. And I'm not holding out for an improvement anytime soon.

So, it became clear that I need to pivot to a different piece of software, which is challenging, because Audacity occupies a really nice niche as a prosumer audio tool with the power you need and nothing you don't. Since the tools below it can't do what I need or are poorly designed, I had to move up to a full digital audio workstation: Ardour.

Ardour is _absolutely overkill_ for what I'm doing. But, it's battle-tested software that people have used to record and produce albums. If I can get over the learning curve, I know I'll be able to get it to work. And for working through the learning curve, importing some records on a USB stereo input is a nice test case actually.

Just last night, I was able to work through the lovely [Ardour tutorial](https://prokoudine.github.io/ardour-tutorial/en/) and get a couple of takes of my 2021 pressing of Gerry Mulligan's Night Lights! Next, I'll need to see about editing down each track to its own file and mastering them. Since I'm just reproducing the recording off the record, it should require basically nothing, but I'll learn the flow.

And as a musician, the investement I make into this piece of software won't be wasted. I may be able to use Ardour to create something in the future.

#### New Headphones 🎧️

As a remote worker, I've been trying to sort out my set up. If my wife is working, I have a noisy kid around. If she's not, I may still have a noisy kid around. If I leave to go to a coffee shop, I need to get in the zone with some good headphones.

I tried to solve this a while back with some Raycon Work earbuds, which include active noise cancelling and advertise an 8 hour battery life (times three, with recharging from the battery in the earbuds' case). But after a warranty claim on the first set, the second set still falls far short of that claim: the left earbud lasts maybe 20 minutes, and the right maybe two hours. 

I still use them for listening to audiobooks as I drift off the sleep, they're great for that. But I've had them die on me in the middle of way too many video calls to trust them for work. 

I had a great set of Bose active noise cancelling headphones back in the day, and that was what I was originally shopping for before I ran onto the more affordable Raycons. Bose has their own noise cancelling earbuds, and I imagine they're better than the Raycons, but they only claim a 6 hour battery life. Even if that is correct, that's not going to quite get me through a work day. But come on&mdash;how much can we really expect from a lithium battery small enough to fit in your ear?

So I notice that Costco had a sale going on the full-sized QuietComfort headphones, and I sprang for them.

I didn't enjoy the fact that there was no manual or quickstart guide included (though of course there was a booklet containing legal warnings etc. in every conceivable language). I had to google around and find the manual, which I've tucked away. What they really want you to do is use their app to set it up. 🙄️

That aside, these sound great, and my first day with them I went through a spring meeting, no problem. Hopefully these will help me be more flexible about where and how I can work and focus.

#### New Work Laptop On the Way! 🙌️

Lastly, I'll celebrate that a new work laptop is on the way! The unit I have currently is about seven or so years old, runs Windows 10 and has 8GB of memory. It can do what I need it to do, but it sits at capacity doing so. And now that I'm working on our company's Remix app and I'm rebuilding that ~30 times an hour, _boy_ am I feeling the limits of this machine. It takes anywhere from 45-75 seconds to rebuild. That makes checking trivial changes rather arduous, no?

Turns out all you need to do to solve this problem is try to demo something you've been working on in a sprint meeting with the head of IT present. He'd started shopping before I was even done presenting. 😅️

I'm told I'm getting a Dell XPS 15 with 32GB of memory. Quite an upgrade! I've eyed the XPS laptops from the sidelines for a long time, but this will be my first time using one. I'm excited to report back when it finally shows up in about a month or so.