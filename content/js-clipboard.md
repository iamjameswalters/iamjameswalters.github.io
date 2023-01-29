Title: Insecurely Copying Text in Javascript
Date: 2023-01-28 
Author: James Walters
Category: Web
Tags: Javascript, _hyperscript
Status: draft

I've been working on an internal web app at my job for our call and chat agents. There's some text provided there that agents commonly need to copy and paste. I thought it might be nice to write a bit of scripting to automatically copy these bits of text to the clipboard when the text is selected, without having to Ctrl-C.

After perusing the web, the obvious answer seemed to be to use the [clipboard API](https://devdocs.io/dom/clipboard). In order to copy text, you would just write something like: 

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


This [MDN article](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard) is a great resource on this topic.