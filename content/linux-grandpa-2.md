Title: Confessions of a Linux Grandpa: An Oral History #2
Date: 2022-09-25
Category: Linux
Tags: Linux Grandpa, oral histories

Hello again Sparky! Have you come for another story about the glory days of desktop Linux? Well who am I to disappoint? 👴️

Now, where did we leave off? Oh yes! I was running Ubuntu on the old Toshiba...

## Grandpa, what was Ubuntu like?

![Gutsy Gibbon]({static}/images/ubuntu-7-10-gutsy.png)

This was Ubuntu, at the end of 2007. It was just then three years old. 

It was [Gutsy](https://en.wikipedia.org/wiki/Ubuntu_version_history#Ubuntu_7.10_(Gutsy_Gibbon)). It was [human](https://en.wikipedia.org/wiki/Ubuntu_philosophy). It was <span style="color: orange">orange</span>. 

And, it made [this sound](https://www.youtube.com/watch?v=NL3c4l6G6pM) when you logged in.

What you're looking at there in terms of the desktop is [GNOME 2](https://en.wikipedia.org/wiki/GNOME#GNOME_2). It offered split panels, one at the top for application menus and launchers (as well as task bar applets), and one on the bottom for window management and virtual desktops. 

Ah, how I *love* those menus&mdash;instead of cramming everything into one Start menu on Windows, here I had three distinct menus: one for applications, one for locations and folders on disk, and one for settings. 😙️🤌️

It came with Firefox 2, by the way.

I mentioned previously that my wireless card didn't work on this release: in order to get it working, I had to download the Windows driver from Realtek and install it with [`ndis-wrapper`](https://en.wikipedia.org/wiki/NDISwrapper). This was a common problem in those days, it would be a few years before the wifi situation improved on Linux. As for this laptop, a driver would make its way into the kernel in the very next release&mdash;it worked out of the box in 8.04 Hardy Heron.

Speaking of installing stuff, there was no "app store" like there is these days, Ubuntu Software Centre [sic] or GNOME Software or whatever. Back then, you had [Synaptic Package Manager](https://en.wikipedia.org/wiki/Synaptic_(software)), which was itself rather new still. It is, essentially, a graphical browser of the packages in the repositories you were configured to use. I still install it on my machines today&mdash;it's quite handy to have around when you need to look at what's inside a metapackage or don't want to have to reach for `apt`.

## We called it "bling" 🥇️

As a devoted Linux user, I was eager to brandish that identity however I could. You might know of a little computer company in Denver called System76. They've certainly come along way over the last 15 years or so. Back in the day, they would [send you some free stickers](https://web.archive.org/web/20080430063103/http://system76.com/article_info.php?articles_id=9) if you sent in a self-addressed envelope. They were a parody of the OS badges that computers came with that said "Powered by Windows XP" and the like. Here's what they looked like: 

![Powered by Ubuntu]({static}/images/powered-by-ubuntu.png)

When I sent for mine, I received not only the OS badges, but also some Ubuntu logos for overlaying the <span style="text-decoration: line-through">Windows key</span> [super key](https://en.wikipedia.org/wiki/Super_key_(keyboard_button)). 😙️🤌️

They don't have the OS badges anymore, but System76 will [still send you stickers today](https://system76.com/merch/stickers).

I also went as far as to register this laptop on some list of registered Linux machines I found out there on the web. The home page would list how many registered Linux computers they were tracking. Of course, this was hardly scientific, it was entirely opt-in and who knows who had actually heard of it? I had discovered it through a badge in someone's forum signature containing their "ID number".

Alas, I'm afraid the name and URL of this site have long passed from Linux Grandpa's memory.

## On the Perils of Dual Booting

I'll close by sharing an early blunder, perhaps my first with Linux.

After installing this and playing around with it for a bit, I decided that I wanted to go back to Windows (this laptop came with Vista). This was only my first foray into Linux, and while I enjoyed it, I was ready to return to the safety of home.

I hadn't [nuked and paved](https://en.wikipedia.org/wiki/Disk_formatting#REFORMAT) Windows; instead, I installed Ubuntu in a [dual boot](https://en.wikipedia.org/wiki/Multi-booting#Microsoft_Windows_and_Linux) setup. This meant that I split the disk into two partitions: one had Windows, the other Ubuntu. Going back to normal should be as simple as wiping out the Ubuntu side.

So, that's exactly what I did. And after completing that operation, I rebooted and...the computer couldn't boot.

The problem? The [master boot record](https://en.wikipedia.org/wiki/Master_boot_record) (MBR) was pointing to something that didn't exist.

The master boot record was a little (512 bytes) sector that told the computer where to boot from. As computers (and kernels) grew to become larger and more complex, the MBR would just point to a bootloader, which would take care of the rest.

Originally, Windows had made the MBR point to its own bootloader. When I installed Ubuntu, it had to rewrite the MBR to point to [`GRUB`](https://en.wikipedia.org/wiki/GNU_GRUB), which would offer boot options for both Ubuntu and Windows.

Well, when I wiped out my Ubuntu partition, I also wiped out GRUB, which meant that the MBR was pointing to something that didn't exist.

Fortunately, with a little Googling, this wasn't *too* difficult to fix: I reached for my trusty Windows install disc, and booted into the recovery utility. From there, I accessed some sort of recovery shell that let me run some command incantation involving a `/fixmbr` flag or something, and it repaired the MBR.

Of course, this was all long enough ago that computers still used MBRs&mdash;do we still use them on [UEFI](https://en.wikipedia.org/wiki/UEFI#Disk_device_compatibility) machines? ¯\\\_(ツ)_/¯

At any rate, this was the first (not the last!) time I got myself out of a Linux pickle. At this early stage, it's a good thing I managed it&mdash;if I'd had to go groveling to my dad and have him fix my computer, he surely would have discouraged me from any further experiments.

That's all for this time, Sparky! As a reward for your attention, enjoy yourself another ASCII Original.

![ASCII Original]({static}/images/asciioriginal.png)

<footer style="text-align: center;font-weight: bold;">
Wait, I'm lost&mdash;<a href="{tag}Linux Grandpa">start from the beginning</a>!
</footer>