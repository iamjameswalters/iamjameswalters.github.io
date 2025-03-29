Title: Checking In Is Fine
Date: 2025-03-29
Author: James Walters
Category: Meta
Tags: open source, ethics, etiquette

There's a post that's a couple of years old called ["Any updates?"](https://justinmayer.com/posts/any-updates/). I saw it recently in [Django News](https://django-news.com/issues/254#start), but I think I've seen it before. It basically discourages you from commenting on GitHub Issues with "Any updates?" since 1) if there were any, they would be in the issue and 2) it's annoying to maintainers for a handful of reasons.

But I felt a bit differently about this, so I thought I'd post about it.

## In Defense of Checking In

I've been the "any updates?" guy on my share of occasions. I want to begin by highlighting an aspect of this post that I found edifying. Asking "any updates" is pretty useless, because he's right, they'd probably be in the issue if there were any. I think a better way to interact here is a comment that clearly shows my interest in the work proposed, especially if it has an encouraging tone. Something like, "This would solve a big problem for me. Would love to see this implemented!"

So, I think the phrase "any updates?" can certainly come across as impersonal, grating, and even perhaps entitled. But also, I think it's good for people to have a way to express their interest and enthusiasm for a thing getting done. I don't think it's really fair to say, "open the ticket and say nothing else, otherwise you're bullying the maintainer". There are lots of people that either can't code but use the software, or can code but not in this stack, or can code in this stack but have obligations of their own that forego being able to contribute directly to this, etc. that would like to see something done, and they ought to be able to say as much.

If this bothers you, I think what you're really saying is that you don't want to address their issue. That might be for several, perfectly fine reasons:

- **You're not interested in maintaining this project.**
    - [Archive it](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)
- **You're only interesting in "maintenance mode" fixes for security bugs, etc.**
    - Say so on your README, and perhaps also on the ticket/issue
- **You're not interested in implementing this particular feature.**
    - Then just say so, tag as `wontfix`, and close the ticket
- **You're not interested in doing it personally, but you're open to it if someone else will provide a PR.**
    - Then just say so, so the rest of us can know there will be no traction here unless someone else steps in and provides some code.
- **You're interested in working on it, but haven't had the time.**
    - Then just say so, and perhaps provide as good an estimate as you can as to when this might get done.

Maintainer burnout is sort of an implied emphasis in this conversation. I care about that sincerely. A lot of people just assume that [open source maintainers will keep the world going](https://xkcd.com/2347/), without so much as a thought as to [whether this person owes you anything](https://world.hey.com/dhh/the-open-source-gift-exchange-2171e0f0). **We should not assume that maintainers must implement every bugfix or feature request we make.**

It's a two-way street though. As a consumer of open source software, I make sure I don't assume that the maintainer of the project can/will/must do X for me. Likewise, maintainers shouldn't assume that people with bugs and requests could/would/should implement it themselves. I'm thankful to be at a place where I can contribute back to many things these days, but I haven't always been, and I might not always be. That shouldn't be tantamount to a revocation of my open source citizenship.

Often, what I really want when making a comment like this is some clue about where we're at and **whether or not I can reasonably expect this to be done.** If not, that's okay, but it means I'm going to have to shift strategies. If I could do it myself and it's this important to me, I wouldn't waste my time asking if someone's going to do it, I would just do it and open the PR.

What I'm really trying to get at with such a question is a decision point: **do I need to go a different direction here?** It's probably a situation where I'm using your library in an app that I'm building. It does 80% of what I want it to do, but there's this big thing missing. It's not trivial, and I can't do it myself. If it's in the pipeline, then awesome. But if it's not, I'm going to have to walk away from this piece of the stack and figure out a different solution. And I'm asking _you,_ the maintainer, to help me understand where your software is headed.

Again, that could all be said more clearly than "any updates," but I don't think the idea of checking in on an issue is out of line.

## In Defense of "Any updates?"

I shared the post in a Discord channel I'm apart of and asked for thoughts. One friend, who works for a big tech company, shared this:

> Both at work and in open-source, I find issues _all the time_ that were never updated, and a meeting, sprint, session, or work in general _is often_ happening behind the scenes! When I (or more likely, the product manager) ask, "Any updates?" there's often a response of "Oh yeah! I forgot to link the PR. Thanks for reminding me!" Or, "Oh yeah! I forgot to paste in the notes from that meeting." But it's not always that work was done - it's also that work _wasn't_ or _couldn't be_ done: "Oops, forgot to change the estimate on this issue," or "Higher priority issues put this on the backlog, will pick it up next sprint," or even just, "We changed our minds [or code, or strategy, or whatever] and don't need this anymore." Worst case scenario, the reply is, "Crap! I forgot about this issue!"
>
> But in every single one of those cases, the prodding of "Any updates?" actually prompted the good etiquette of making sure the issues you own are updated. People reading your issues can't read your mind. You may think, "Well it's obvious I can't get to that right now, it's low priority." But the guy who found the issue while googling the error message he got from your software doesn't know you consider his problem low priority. We all need reminders to put our notes down.

I thought this was a valuable perspective, both as a defense of using the actual question "any updates?" but also because I think my friend put so clearly what I think is at the heart of this issue.

## Communication is the Thing

This is really about communicating well with each other as co-citizens of the open source ecosystem.

I think part of the problem is the quasi-social nature of things like Github. On the one hand, I truly understand the desire of those with the temperament of engineers to keep all conversation on an issue related to implementing the issue, and that _"any updates?/Hope we can make this happen!/This would really help me/etc"_ just creates noise. But where else are people supposed to indicate that? I've had some developers say "+1 the issue", but that doesn't give me any indication of whether you care or are setting any wheels in motion about this.

Maybe we should have more "feedback forums" or some sort of open source equivalent of a suggestion box (maybe [Github Discussions](https://docs.github.com/en/discussions) are a good place to start for projects to have this sort of thing?). I understand that people tend to have widely different assumptions about what's appropriate for a Github issue. But if you really don't want to interact with people about feature requests/bugs, then [turn off Issues](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/disabling-issues). Indicate this on your README. If you're going to be part of an open source community, then you owe it to that community to establish up front what interactions from them will and won't be welcome. That's just loving your neighbor. You don't want extraneous and irrelevant comments on your issues, others don't want to be left in the dark about the status of features that matter to them.

Calm, clear, empathetic and respectful communication from both sides of the ticket is the way forward to better and healthier interactions between maintainers and software consumers.