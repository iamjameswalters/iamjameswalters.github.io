Title: Insecurely Copying Text in Javascript
Date: 2023-04-11
Author: James Walters
Category: Web
Tags: JavaScript


I've been working on an internal web app at my job for our call and chat agents. There's some text provided there that agents commonly need to copy and paste. I thought it might be nice to write a bit of scripting to automatically copy these bits of text to the clipboard when the text is selected, without having to Ctrl-C.

After perusing the web, the obvious answer seemed to be to use JavaScript's [clipboard API](https://devdocs.io/dom/clipboard). In order to copy text, you would just write something like: 

```javascript
navigator.clipboard.writeText("text I want to copy")
```

And indeed, this will work in something like 90% of your usecases. I ran into an edge case though.

## Let Me Stop You Right There 🛑️

You see, the use of the clipboard API requires a [secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts). What exactly does that mean? It's probably a bit more nuanced than this, but _basically_ it means you need to be connecting over HTTPS.

Remember how I mentioned this was an **internal** web app? We access it unencrypted. That means the clipboard API won't work. 😩️

Is there any other way?

## I'll Copy Whatever I Darn Well Please 

It turns out there kind of is.

This [MDN article](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard#using_execcommand) is a great resource on this topic. There's a deprecated API called `document.execCommand()` that allows you to do all kinds of things, one of which is `copy`. But if it's deprecated, how can we use it?

The key is in this condition (emphasis mine):

> These commands can be used without any special permission in **short-lived event handlers** for a user action (**for example, a click handler**).

That's exactly our usecase. I'm assuming this API wouldn't work if you had it as part of a script. But as part of an `onclick` handler, the browser will execute it.

Running `document.execCommand('copy')` will copy whatever the currently selected text is to the clipboard, so you have to manually query for the element you need, call its `.select()` method to have the cursor select its text, and then call `document.execCommand('copy')`, which is a little cumbersome. In my case, I've got some CSS applied to a `<span>` such that whenever you click anywhere inside it, all of its text gets selected. That just leaves the copy logic. My code looks something like this:

```html
<!-- span containing text to copy -->
<span 
  style="user-select: all;"
  onclick="document.execCommand('copy')">
  Copy this text
</span>
```

It's possible you could encounter a race condition where the command gets executed before the CSS, but that's never happened in any of my testing. Anyway, the solution would be to add a 50ms pause or something barely noticeable like that before running the command to give the CSS time to be processed.

Try it yourself! 
<div style="text-align: center;margin: 30px 0;">
<span style="user-select: all;" onclick="document.execCommand('copy')">
  Copy this text
</span>
</div>

Did it work for you?

Anyway, that's how you can copy-and-paste something in JavaScript if you can't use `navigator.clipboard` for whatever reason, like serving from an "insecure context". I suspect serving web pages over unencrypted connections is still common enough for things like internal intranet sites that someone might need to know about this.

<footer style="font-weight: bold; text-align: center;">
Found this helpful? <a href="https://ko-fi.com/iamjameswalters">Buy me a coffee!</a> ☕️
</footer>
