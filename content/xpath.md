Title: The Road Less Traveled: Understanding XPaths
Date: 2023-01-26
Category: Web
Tags: Selenium, XPaths, Web Scraping, HTML, XML
Status: published

The other day I started writing a web automation tool to do some chores for me at work. This was my first time using [Selenium](https://www.selenium.dev/), a handy dandy library for driving web browsers in code.

When it comes to getting a hold of elements in the page you want to interact with, Selenium offers the usual ID and class-based CSS selectors. Since I was trying to navigate a page written in React though, most of that information was [randomly generated](https://www.reddit.com/r/webdev/comments/lucdnp/why_are_class_names_like_this_in_facebook_and/). I needed to get at elements by grabbing onto an easily accessible anchor, then using it as a reference point from which to step through the document tree and get at what I was looking for. Since it's 2023, I of course expected to use some facsimile to the [Javascript DOM API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction). A `.parentElement` here, a `.firstChild` there, and I'd be able to grab that pesky button nested within three generic `<div>`s and click it. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) works this way, why wouldn't Selenium?

It turns out that, no, Selenium does *not* work this way. For whatever reason, instead of something resembling the DOM API, Selenium uses [XPaths](https://en.wikipedia.org/wiki/XPath). When I first started trying to write these things, they struck me as a bit ersatz, landing somewhere along the spectrum between filepaths and regular expressions. But I have to say, they've grown on me a bit, mostly because they're far and away the best tool Selenium gives you for finding elements on the page. 

## Happy Little (Document) Trees 🌳️

XPaths (the XML Path Language) are based around the idea of seeing the HTML document as a tree of nodes. Let's take the following HTML for our examples:

<pre><code class="language-markup">
<script type="prism-html-markup"> 
<html>
  <body>
    <h1>Hello World!</h1>
    <p>
      I'd like to welcome you all to this web page. Check out my stuff!
    </p>
    <p id="label">Things I like:</p>
    <ul>
      <li>Cats</li>
      <li>Video games</li>
      <li>Pizza</li>
    </ul>
    <button>
      <span style="font-weight: bold;">Enjoy this page?</span> Let me know!
    </button>
  </body>
</html>
</script></code></pre> 

If we wanted to write an XPath to target the header at the top of the page, we might write something like this:

```
/html/body/h1
```

Let's break that down. The opening slash `/` means the root of the document, the beginning of everything. This is very similar to the root `/` in [UNIX filepaths](https://en.wikipedia.org/wiki/Root_directory). There's only one element in the root of our document: `<html>`. So, that's what we type next. Then, within the `<html>` tag, we select the `<body>` tag, and then the `<h1>` within it. Because this XPath starts at the root of our document and walks through nodes in the tree to get to the one we want, it's kind of like an absolute filepath.

Pretty straightforward. But, here's another way we could get at that header:

```
//h1
```

What's going on here? Whereas the single slash `/` means that what comes after it must be immediately within the node that comes before the slash, the double slash `//` means that it should be *somewhere* inside it. It allows us to find things that are nested a few layers in. So in this case, we're looking for an `<h1>` that's somewhere within the root of the document.

Here's another example of this in action:

```
/html/body//span
```

This XPath says that in the root of our document there should be a `<html>` node, and within that a `<body>` node. Then, *anywhere* within `<body>`, we want a `<span>`. This would select the `<span>` from our example, even though it's inside a `<button>`.

So far our XPaths have only matched one node in our document. But what do we do if we want to select a specific item from a handful of nodes that match our XPath? Let's look at our next example:

```
/html/body/ul/li
```

You probably guessed that this XPath selects an `<li>` node in our unordered list. But which one? That XPath matches all three list items (and left this way, would return them all). 

We can use an index to get at a specific node matching the XPath. If we want to select "Video Games", we can modify our XPath this way:

```
/html/body/ul/li[2]
```

Note that XPath indexes are **not** like Python indexes&mdash;they start at `1`, not `0`.

## Predicate Predicaments 🤔️

Those brackets `[]` in the last example constitute a predicate clause. They allow you to specify something that should be true about the element your selecting. In this case, we were specifying that the `<li>` we select should be the second child of the `<ul>`. 

There are other predicates available for us. For instance, we can predicate based on an element's property:

```
/html/body/p[@id='label']
```

This XPath selects a `<p>` node that has an `id` property with a value of `label`. 

You might also be wondering, is it possible to select the value of the `id` itself? Why yes, you can!

```
/html/body/p/@id
```

This XPath would select the value of the `id`&mdash;that is, it would return the string `label`.

A particularly helpful predicate we can use is checking an element's text with the `text()` function. For example, if we wanted to select the list item that says "Cats", we could do so like this:

```
//li[text()='Cats']
```

Note that this will only work for an *exact* match. The entire text must be "Cats". If you want to check if an element's text *contains* something, well, you'll need the `contains()` function:

```
/html//p[contains(text(), 'like')]
```

The `contains()` function takes two positional arguments: the first for the thing to check, and the second for the value to look for. In this expression, we're looking for a `<p>` element whose text contains `like`. Since both `<p>` tags in our example have the word 'like' in them, they both get selected. 

Predicates can also be chained. If we wanted to narrow down our selection to the `<p>` with `id="label"`, we can add that predicate:

```
/html//p[contains(text(), 'like')][@id='label']
```
<!--
Actually, there's another issue lurking here, one that gave me quite a headache.

If we wanted to try and select our button based on it containing the phrase "Let me know!", we might try this:

```
//button[contains(text(), 'Let me know!)]
```

But this won't work. How come?

After some spelunking, I came across a [Stack Overflow answer](https://stackoverflow.com/questions/3655549/xpath-containstext-some-string-doesnt-work-when-used-with-node-with-more) (of course) that explained it. I'll leave the details of that answer to you, but to sum it up, because the button contains not just text but a `<span>` element as well, `text()` returns a *list* of nodes. We then want to check *each* of those nodes (one of which is the "Let me know!" text) for a match of our string. In order to do that, we need something like this:


-->

## Additional Resources 📚️

We've only scratched the surface of XPath syntax. If you're looking for a deeper dive, I found the cheat sheet at [devhints.io](https://devhints.io/xpath) incredibly helpful. Not only does it get into a wide variety of XPath syntax, but it also offers some translation between query paradigms you might be more familiar with, such as CSS selectors or JQuery. It has some helpful notes about a few gotchas in there&mdash;think you know how to write an XPath querying an element's class? [Think again!](https://devhints.io/xpath#class-check)

Finally, I think that the single best tool for wrangling with XPaths is hidden within your browser's devtools. I've yet to check Firefox, but using Chromium-based browsers like Brave and Edge, I learned that you can inspect an element, right-click on it in the code view, and under the "Copy" option, you can copy an XPath for that element. This can help a lot if you're trying to figure out how to write an XPath for something in Selenium! 

![Right-click to copy an element's XPath]({static}/images/xpath1.png)

Also, using Ctrl-F in that inspector will let you test out XPaths and see which elements on the page satisfy it&mdash;just write your XPath in the Ctrl-F dialog and massage it until it selects what you're looking for.

![Type XPath expressions right into Ctrl-F to test]({static}/images/xpath2.png)

So there you go, a whole different way to navigate HTML documents that was hiding right under our noses. The XPath road may be less traveled than the DOM highway, but I think I might be taking it a little more often from now on.