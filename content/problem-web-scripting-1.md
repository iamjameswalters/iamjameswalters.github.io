Title: Web Scripting: Its Problems and Solutions #1 - Javascript
Date: 2022-10-11
Category: Web
Tags: web scripting, Javascript, JQuery
status: draft

Sometime back in the mid-00s, I started toying around for the first time with the web. I owe my fledgling years to [W3Schools](https://web.archive.org/web/20070225131938/http://www.w3schools.com/). I began with HTML, which was easy enough to pick up. This was back before [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns#HTML,_CSS,_JavaScript) and [semantic markup](https://en.wikipedia.org/wiki/Semantic_HTML) were entrenched standards and you were allowed to use things like `<font>` tags. You could use just HTML and get pretty far, but eventually you reached for CSS, which was a bit different, but not too bad. They both follow a nicely descriptive and declarative paradigm that is fairly straightforward to grasp.

Having made satisfactory progress in these domains, it was time to conquer the next frontier: Javascript. This was particularly exciting, as I was told this was where you could create powerful, dynamic behavior on your webpage. 

Things started well enough. I got to a lesson that involved doing some basic math, and building a calculator in the page. Wow, I'd made a real thing! This was kind of neat. 

I did `3 + 3`. It gave me `6`. Huzzah!

I hit `+ 3`, it answered back `9`. Beautiful!

I hit `+ 3`. It answered `11.98`. [Eh wha?](https://www.youtube.com/watch?v=RlbARlVyRAc)

The nuances of floating-point arithmetic were lost on my young mind&mdash;this was just irritating enough for me to throw up my hands and abandon the entire project of learning Javascript.

## The Problem with Web Scripting

Scripting on the web is hard.

Part of the problem is the rather ugly fact that scripting on the web is _necessary_ for design patterns many people are after. It's impossible for instance to make a [single-page application (SPA)](https://htmx.org/essays/spa-alternative/) without scripting. The indeterminate state of a check box can [only be set with Javascript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox#indeterminate_state_checkboxes). Even beyond such implementation issues, there is a cultural tide that assumes you'll be doing scripting if you're doing anything on the web. I find this quite irritating for the following reasons:

- Javascript should be [unobstrusive](https://en.wikipedia.org/wiki/Unobtrusive_JavaScript), but just turn it off in your web browser and see how often that missing funcitonality gets in the way.
- Related, web developers should (but generally don't) seek [progressive enhancements](https://en.wikipedia.org/wiki/Progressive_enhancement) that degrade gracefully. This is important since [~1% of all users don't receive the javascript](https://youtu.be/rxlJRydqmk8?t=360) they should be getting.
- Code-on-demand is [supposed to be optional](https://htmx.org/essays/hypermedia-driven-applications/).

This last one matters a lot to me. I'm a firm believer that you should ***not*** have to be a programmer in order to make a web page. You'll certainly need to be a programmer to make a web _application_, but a web _page_, even a web _site_ composed of such pages, should be possible to make without having to understand the abstractions of programming. Call me a bleeding heart, but it's my right to hand-write piles of HTML files and stuff them on a web server, even if it's less efficient than using a static-site generator.

Thankfully, this is a lot easier than it used to be. You can do some amazing things with pure CSS these days thanks to [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes), [animations and keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes), etc. Support for HTML5 widgets (like [&lt;video&gt;](https://www.w3schools.com/tags/tag_video.asp) and [&lt;input&gt; types](https://www.w3schools.com/html/html_form_input_types.asp) like `date`, `datetime`, `color`, and other things you traditionally built some JS widget for) has been a huge boon. But can you make, say, a modal dialog without using any JS? I mean, [I guess so](https://codepen.io/Idered/pen/DdeoeW), but not without some CSS ingenuity.

Even granting that it's technologically possible to create most of the common design patterns a typical person would expect with mostly HTML5 and CSS3, there's still a pervasive culture that JS is just a requirement for the modern web, and you should assume you should use it, and everyone assumes you can write it.

But, Javascript is hard to write, which brings me to my next point.

## The Elephant in the Room 🐘️

You'll notice that I've been using the term "web scripting" and Javascript as loose synonyms. That's because Javascript is the only language you can use for web scripting. I don't like that.

Here are a handful of reasons why:

- Javascript uses floating-points for numbers. Don't know what that is? You shouldn't have to. They're _numbers._ They should work like _numbers._ When I add `3 + 3 + 3 + 3` I should **not** get `11.98`.*
- It has noisy syntax. `{ }` Curly braces delineate most code blocks, `object.methods()` are everywhere because Javascript was written in the 90s when [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming#History) was a ~~fad~~ obsession, and you have to end every line of code with a `;` semicolon. [Except you don't](https://en.wikibooks.org/wiki/JavaScript/Automatic_semicolon_insertion). [Except you do](https://betterprogramming.pub/you-might-need-those-semicolons-in-your-javascript-after-all-b28154f93ea8).
- Its typecasting is a total mess. Try to add a string and a number, and it'll typecast the number into a string. `'1' + 2` returns `'12'`. 
- Arrays are a horror. Using `delete` against an array value doesn't work as I'd expect it to in, say, Python. It just blows a hole in the array. (i.e. `delete`-ing `'B'` from `['A', 'B', 'C']` returns `['A', empty, 'C']`, instead of `['A', 'C']`, which is what I probably wanted). Thanks to [Chris Trudeau](https://realpython.com/courses/python-vs-javascript-for-python-devs/) for teaching me that one.

Now, these issues might not be that big of a deal to you. You might even _prefer_ some of these things. Well and good. Every programming language is a little bit different. They all have different styles, and you can use your language, I'll use mine, and we'll all get on our merry way.

Except on the web. Here, it's Javascript or the highway.

This is supremely irritating. If I'm writing a web app, I can do that in nearly any language: Python, Ruby, Rust, PHP, Perl, Go, and yes, even Javascript. But no matter which of those languages I use on the backend, I'm still married to JS on the frontend.

Why does it have to be this way? Why am I bullied into using a language whose syntax I find difficult to read, and whose type behaviors I find confusing and unexpected? At least its cousins in the C family offer faster performance for being lower-level languages that are closer to bare metal, but JS is slow by comparison.

So all those problems&mdash;and more, as we'll touch on&mdash;are foisted upon anybody who wants to make a halfway decent looking web page. And they have to understand programmatic abstractions on top of that. Gross. 🤢️

## The Pitch ⚾️

So, here's the idea. In this series, I want to look at some good (and some not-so-good) solutions to how to fix some of these fundamental problems with web scripting. Hopefully, we can find something that makes it less programmer-y and more friendly. 🤗️

I think a perfectly fair test would be my original test: build a simple calculator in HTML/CSS, and script the logic. For everything we examine in our series, I'll build the same functionality as idiomatically as I can to the thing we're using&mdash;this means following conventions like separation of concerns vs writing things inline, writing event handlers or calling functions, etc. I'll try to write code that's as representative as possible of the way that library/framework/tool/thing is _normally_ used.

We'll begin with the topic _d'jeur:_ plain, vanilla JS. 🍦️

## Calculating 🧮️

***

*&nbsp;Which, to be fair, you don't anymore, at least not with that particular example. I'm assuming that's to be accounted for by higher-precision floats being used in browsers more modern than Firefox 3 or IE6 or whatever I was using at the time. 👴️ But, you'll still encounter bizarre quirks that are side effects of this eventually.