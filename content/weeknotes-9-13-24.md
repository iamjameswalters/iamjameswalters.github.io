Title: Weeknotes 9/13: The Unlucky One?
Date: 2024-09-13
Category: Weeknotes
Tags: hardware, Django, Remix, music

Here we are, definitely one week after my last Weeknotes entry. 🙂️ Here's what's going on this week:

#### New Headphone are Awesome 🎧️

Last time I mentioned my new Bose noise-cancelling headphones as a replacement for my Raycon earbuds to help create a more sound-tolerant workflow. They've been great! And I'm quite happy to see that this tech, while still premium, is less expensive than it used to be. Really hoping to do a lot more working from coffee shops and the like.

#### Remix 🔁️

I haven't spent a ton of time on here talking about it, mainly because I'm a Python/Django guy at heart. But at my job these days, I've been brought in to help with our new Remix site.

As you might expect, I have mixed feelings about it. On the whole, I'm really a [hypermedia](https://htmx.org/essays/hypermedia-driven-applications/) guy, and I'm just not a fan of all of the extra complexity reactive frontends add to a site. But my 30,000 foot take is that _if_ you're going to build the whole site out in React, _and if_ you're going to use client-side routing, _and if_ you're going to do server-side generation, then it's a nice choice that usually keeps you more focused on your application logic than with wiring all of that up.

But this isn't a comprehensive review of Remix, I probably don't even have enough experience to do one. I just want to talk about whatever it is that I'm working through at the moment.

At this moment, I've been pounding my head against the wall trying to understand how index routes work, since I had an idea about refactoring a route to use them. In Remix, you're doing nested routing, which means each component gets a route, and usually each component has an `<Outlet />` where the child components get rendered. It basically looks like a telescope. Let's say you're setting up a detail view at something like `app/things/123`: there's some framing stuff around the edges, UI controls or whatnot that are the same for every item, and then the item's specifics get loaded into this parent route's outlet. But what if you just navigate to `app/things/`? I'd like _something_ to live in that outlet until I load in an item's details. The solution to this in Remix is an index route. The documentation says pitifully little about index routes, other than an [example in the tutorial](https://remix.run/docs/en/main/start/tutorial#index-routes).

I had a terrible ordeal getting this set up, but it turns out we use [custom folder routing](https://remix.run/docs/en/main/file-conventions/routes#folders-for-organization) in our app, so it had to be wired up a little differently. 🙃️

I'm still fairly new to understanding a lot of Remix's general patterns, so stay tuned for more.

#### Planning a Django Refactor 🛠️

Aside from the Remix app, for a long time I've desired to undertake a refactor of the first app I ever worked on, which is a Django application. After giving it a lot of thought, I think I've identified the following improvements I'd like to make:

- **Vanilla views** - The hairiest file in our entire project is views.py. We used class-based views over function views, and I don't regret that decision. But I am at the point where I see all of the wisdom that [django-vanilla-views](https://pypi.org/project/django-vanilla-views/) brings to the table. I think we could trim views.py by at least 25%, while also making it easier to understand and reason about.
- **django-auto-prefetch** - I took care of the worst N+1 bugs in our app during development, but there are still some that remain that simply aren't noticeable yet because those views don't handle enough data to make them a pain point. In my opinion, this is one of the worst rough edges of Django, and I really think we need a solution built directly into the framework. N+1 bugs are very nearly a design feature of the ORM. Back when I was tracking these down with django-debug-toolbar, I caught most of them, but there were still some that I couldn't track down. Although I don't just want to paper over problems and I'd like to learn how to write better ORM code, at this point I'm interested to see if [django-auto-prefetch](https://pypi.org/project/django-auto-prefetch/) will solve these harder to pin down bugs. If it does, hats off to Adam Johnson!
- **Template complexity** - one of the weak points in our current app is the way the templates are arranged. The main reason for that is that we were experimenting and learning htmx at the same time, and we were trying to figure out what the best patterns were. Where that's left us today however is a place where we have a fair amount of duplication across our templates, with some being rendered on initial page loads, and other parts of the page getting fetched again by htmx. I need to take a look at [template partials](https://pypi.org/project/django-template-partials/), [includes](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#include), etc. and find something to deal with template complexity and make things more DRY.
- **Form errors** - I was lazy and built a lot of forms without proper error rendering, so many forms will just appear not to do anything if they had an error in their input. This was tolerable only because the two people using the editing interface (where all the forms are) of this app were the people developing it. 🙂️ But it's still a shortcoming, and one that ought to be fixed easily enough.
- **Unique constraints** - related to the former, we developed our app on top of Django 4.0. In 4.1, we got the wonderful added feature that [unique constraints on models would now be included in model validation](https://docs.djangoproject.com/en/4.1/releases/4.1/#validation-of-constraints) (instead of operating merely at the database level). This means that instead of getting a DB error when you tried to save (which would throw an exception that would 500 your user if you didn't handle it), it would now fail in the model validation which would bubble back up to your user in a form error. Huzzah! Less work for me! The problem, though, was that we aren't using an officially supported database: we're using Microsoft SQL server, which means we use Microsoft's [mssql-django](https://pypi.org/project/mssql-django/) backend. And the new unique constraint model validation was not supported in mssql-django. ☹️ So at the time, I gutted all the extra unique constraints that were just blowing up with 500s. These days, however, that support has been added, so now I should go back and add a bunch of unique constraints.

I can only undertake these tasks as time permits, and I'm not sure I'll find time even before the end of the year, given the hustle we're in to get our Remix app out the door. But the planning has been valuable, and shows the fruit of experience that I didn't have when first I worked on this project.

#### Learning Piano Scales 🎹️

On a non-tech front, I've been on a slow journey to ramp up my proficiency at the piano. I have a long background in music, but mainly singing, and I'm a mediocre guitarist. Having decided I've plateued with the instrument, I'm looking to lean into the keys. There are several reasons, not least of which is the fact that if you're proficient at the keyboard, you can use software to make all kinds of music these days. It really is the one instrument to rule them all.

Anyways, I've learned a couple of things recently that I thought I'd share.

##### Understanding scales in the flat keys

The place for me to begin is getting an elementary understanding of all the major scales. Scales will be a part of my practice routine until the day I die, so I'm not looking to be at a high level with them out of the gate, but I'd like to know and understand the proper technique to play them for all of the pitch classes.

I started with C major (no sharps or flats) and started building my way through the sharp keys, adding one sharp at a time. This was easy to wrap my head around: you're just playing the white keys, except whenever you encounter a sharp, which means you raise your finger up to a black key. I did this all the way through B major (five sharps).

But the flat keys were a different story. I started with Gb major (seven flats), and as I moved to Db major and Ab major, I found I couldn't keep my fingerings consistent. It finally dawned on me that the best way to think about the flat keys is that Gb major is the fundamental "shape" of the flat key scales&mdash;that is, the fingerings you use in Gb are the ones you want to use everywhere, but as you remove flats from the key signature, those become the exceptions. 

The effect of this is for instance, in Gb, I play Gb-Ab-Bb (the cluster of three black keys) with my 2nd, 3rd, and 4th fingers. The secret for me was realizing that in whatever scale you're in, you should _always_ play those notes with those fingers. As you start removing flats, you'll move those fingers down to white keys, but whenever I play Bb for instance, I should always aim to play it with my 4th finger, from Gb (seven flats) all the way down to F (one flat, the Bb). Doing so will keep my hand in the right place for playing the rest of the scale, particularly in descending directions (in the right hand, anyway).

##### There's no shortcut for sightreading

Once I've got a command of my scales, I'll be looking to throw myself into sightreading. I've been a musician long enough to know that there are two kinds of people: those who can read music, and those who can't. This is a topic of its own, which I cannot afford to plunge into here. Suffice it to say that I find a fair analogy in literacy and illiteracy (or preliteracy, if you like), with similar advantages and liabilities to each. But aside from the importance of learning to sightread, I also understand the importance of learning to sightread _early:_ not unlike reading, the longer you wait to get started, the harder it will be and the slower you will make progress. Learning to sightsing was a challenge. I couldn't read a guitar part to save my life. I'm hoping to get started firmly on the right foot with piano.

I'm hoping to play out of my hymnal for my small group soon, and as my hymnal has chords notated in it, I thought one day, "maybe I should just fast-track my way to learning all the chords, and then I start playing out of the hymnal with the chord notations." 

After turning it over though, I quickly realized that this would be quite a challenge. It's one thing to learn a bunch of triads, it's another to learn all the _voicings_ you can use with a chord. And it's yet another thing entirely to understand how to choose the right voicings to navigate the progression in front of you. You have to develop a strong and intimate knowledge of these things before you can compentently play your way through a chord chart.

How do you develop that? The best answer is by playing other people's music. Composers and arrangers are really good at thinking through intelligent ways to voice things. And the best way to start to internalize that and develop your own intuition about how to voice chords is to play music that is well written and arranged. 

And how do you play other people's music? Well, you have to _read_ it. And the better you are at sightreading what's on the page, the easier it will be to get on with playing all the music that is going to start shaping your playing and developing your musical intuition.

There is no shortcut for sightreading.

But once you can, it's worth mentioning that a hymnal is a _fantastic_ collection of bite-sized tunes with excellent melodies that are expertly arranged (in many cases over centuries). The average hymnal contains 400-700 tunes. Whether you're religious or not, this is a goldmine of sightreading material.

#### Fin

Thanks for reading, see you next week!