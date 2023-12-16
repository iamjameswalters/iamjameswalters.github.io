Title: PyOhio 2023 Slides & Resources
Date: 2023-12-16
Author: James Walters
Category: Python
Tags: Scrapy, web scraping, PyOhio, portfolio

On the heels of DjangoCon (sorry, a restrospective is overdue for that one, it's coming, I promise), I went and signed up for another conference&mdash;[PyOhio!](http://pyohio.org/) 

I decided to throw my hat in the ring with a talk on web scraping. It's a fun skill that I've put to use in a few different situations so far. Getting this down to 15 minutes was __hard!__ My first talk was in person at a conference, but this conference was online, which was a different experience. It was harder putting together a video I think (I'm used to public speaking), but it made for a stress-free conference day!

If you're reading this, I hope that means you enjoyed the talk and came here for some pointers to some related resources. Here they are:

- [My talk page on PyOhio.org](https://www.pyohio.org/2023/talks/web-scraping-crash-course-with-python-and-scrapy/)
- The [Github repository](https://github.com/iamjameswalters/library-eventextractor) for the demo code I wrote in the talk
- [My slides](https://docs.google.com/presentation/d/1kzZ2Jppvm9gudBCYFTHiEAamP6qjdnC17ONPA6FR0WI/edit?usp=sharing)
- My [post on XPaths]({filename}/xpath.md) that explains how these work
- [Scrapy's documentation](https://docs.scrapy.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), an HTML parsing library. Handy if you're dealing with ugly, malformed markup. I'm honestly more accustomed to BeautifulSoup's API and would probably reach for it instead of using the Scrapy's built-in selectors.

I'll also include a few things that I had to cut from my talk due to time constraints.

### Is Web Scraping Legal? 

The answer to this is that, while there are some limitations, yes, web scraping is legal. Here are a couple of articles that get into the concerns in more detail, but yes, as long as your respecting others’ copyright, and you’re scraping publicly available data, there’s nothing illegal about that. 

- [TermsFeed - Web Scraping Laws](https://www.termsfeed.com/blog/web-scraping-laws/)
- [Electronic Frontier Foundation - Victory! Ruling in hiQ v. Linkedin Protects Scraping of Public Data](https://www.eff.org/deeplinks/2019/09/victory-ruling-hiq-v-linkedin-protects-scraping-public-data)

### Scrape Politely 😁️

It’s worth mentioning though that there are some points of etiquette to consider.

#### 1. Robots.txt

The first rule of etiquette when web scraping is respect a website’s robots.txt. Robots.txt is a file that tells web crawlers like search engines and your scraper what kinds of things they should look at and what they should not. It’s always a good idea to follow a site’s robots.txt.

#### 2. Terms of Use

The second rule is to respect a site’s Terms of Use. Even if you’re accessing publicly available data which is legal to do, you may be accessing data in a way that violates a site’s Terms of Use. In these cases, you may not have any legal liability, but you may get banned from the site.

#### 3. Wait a bit between requests

And finally, a third rule of thumb to follow is, if you’re scraping several URLs on the same site, space those requests out a bit and add some wait time in between. If you’re hitting a site with a bunch of requests out of nowhere, that’s something that a lot of sites are going to interpret as the beginning of a denial of service attack rather than legitimate use, and you might get autobanned for a bit. So don’t overload a site’s resources or come at them by surprise: set up your scraper to wait a bit in these cases.

### Where Do I Run My Scraper?

So now that you’ve written a web scraper, where should you run it? It’s easy to run scrapers on a one-off basis like we did in the talk, and if that’s all you need to do then this isn’t a problem for you. But you probably want to do some routine capturing of data, what’s the best way to do that? 

The easiest way is to schedule it as a scripted job on your own computer. In Linux you can do this with a cron job, on Windows there’s the Scheduled Tasks system. I have a scraper that runs on my work laptop every morning to gather up some non-critical data I keep an eye on for my job.

Another option, if you want something going twenty-four hours a day, is to deploy something on a cloud box. Or, a great variation on this is to stand it up on a Raspberry Pi. I have plans to set up a web scraper on a [Raspberry Pi Zero](https://rpilocator.com/?cat=PIZERO%2CPIZERO2), it’s a tiny $15 computer that uses around one or two watts of power. It’s a great little tool to run a web scraper on.

### What Should I Scrape For?

Now that you know how to scrape the web, what should you scrape for? There are lots of great ideas out there, you can google for them all day long, but a great place to start is your next job. It’s really easy to scrape job sites using these tools and you can have something always looking for that next big career opportunity for you. Searching for jobs is one of the most laborious parts of your career search, so why not automate that chore? Let the jobs come to you.

This applies to your next house or car as well, you can scrape real estate listings, apartment sites, and car dealerships for find your next dream car or dream home.

### Conclusion

I hope this has been informative and helpful. Web scraping is one of those programming things that I would have thought was beyond my reach, but actually it's quite doable, and it comes in handy even more often than you think. Happy scraping!


<footer style="font-weight: bold; text-align: center;">
Found this talk useful or insightful? <a href="https://ko-fi.com/iamjameswalters">Buy me a coffee!</a> ☕️
</footer>