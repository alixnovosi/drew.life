Title: Side Projects Are Fun
Category: Dev
Tags: side-projects
Author: drew
Date: 2017-11-10 04:25:08
Modified: 2018-12-03 21:50:14

I spent a lot of time on programming side projects in 2016.
I'm finishing this post up in 2017 after writing the bulk of the text,
so please forgive any confusing year references.

### Side Projects
There are always things I'm tinkering with.
Until recently,
it's been silly scripts and my Haskell-powered window manager's config file.
Other times,
I've worked on polishing or fixing class projects,
or getting things nicely set up with GitHub and Travis CI so I can feel like a Real Developer™
This has happened ever since I learned to program properly in college,
so for about 5 years now.

My side projects in 2016 were a lot more solid.
There are some more specific reasons for that,
but I think the more general one is that I started a full-time software job.
I've started to treasure free time a lot more,
because I don't have a ton of it after work and commuting and preparing dinner.
That in turn drives me to want to complete things in my free time,
to feel like I'm Doing Things.
There's a balance,
of course,
but I'm happier when I can tell myself I'm making progress on something.
I track what games I'm playing,
so I can see how many games I've stuffed into my free time over the course of a year.
I have a podcast backlog and I work on cutting that down
(hit me up for recommendations).
And,
because I'm a software developer,
I try to work on projects that I can measure progress on in a meaningful way.

### puckfetcher
The more direct reason for my first project -
a podcast downloading app -
was driven by problems with every podcast app I found.
I listen to my podcasts basically exclusively on a laptop,
because I have one within reach basically all the time.
I work on a Mac,
and use a Linux-running ThinkPad as a personal laptop,
so I need something cross-platform.
I tried [Newsbeuter](http://newsbeuter.org/) for a while.
Newsbeuter has a lot of functionality,
which is neat,
but made it really hard to figure out to use it.
I tried gpodder for a while,
but it got really slow when I tried to download big podcast backlogs,
and at some point it just broke for me.

> gpodder has been broken on downloads for me for weeks
>
> — [@alixnovosi](https://twitter.com/alixnovosi/status/684110565845774336), 2016-01-04 12:34 PM

I kept downloading by hand,
and for a while I was OK with that.
I kept up on some of my podcasts
(the Giant Bombcast,
the Giant Beastcast when it started),
and dreamed of listening to others.
Early in 2016,
though,
I finally got tired of it.

> I'm going to drink tea, watch AGDQ, and try to write a Python podcatcher that finally works for me.
>
> [@alixnovosi](https://twitter.com/alixnovosi/status/684252794140807168), 2016-01-05 9:59 PM

Unfortunately,
the exact moment and motivation that got me actually doing the work is lost to time.

I worked on [Puckfetcher](https://pypi.python.org/pypi/puckfetcher) for essentially all of 2016.
It started out really simple -
I ran it and it started downloading episodes from the backlog of some podcast I hardcoded into it.
Next,
I set it up to just take a URL and give me the latest episode of that podcast in return.

The early days of a new project are fun,
I found out.
I spent a lot of time trying things and seeing what happened.
I learned my way around [feedparser](https://pypi.python.org/pypi/feedparser),
which does basically all of the work to handle podcast feeds.
I worked out how to use [requests](https://pypi.python.org/pypi/requests) for downloads.
I knew Python from school,
but I looked up best practices and did my best to stick to them.

Deciding on the structure of what became puckfetcher was more work and more interesting than I expected.
Some assignments in college started me from nothing,
but the structure I was supposed to build around was always given.
For puckfetcher,
it was always up to me.
I created a Subscription class to handle the idea of individual podcasts I wanted to listen to.
I taught them how to update themselves,
how to parse some YAML from a user config file,
how to encode themselves so I could save state.
I build a Config object to handle a whole set of Subscriptions,
and taught that how to read a config file and save and load and update all of the podcasts.
I even set up a Util file with stuff that I thought I could eventually reuse somewhere else
(and some of that did eventually get reused).

Unfortunately,
I didn't program puckfetcher perfectly,
and I had some exciting errors and bad approaches.
For a long time,
I had this idea that keeping track of a podcast's schedule was the best way to download episodes on time.
The user would put in what days of the week the podcast aired,
and when you told puckfetcher "give me more podcasts" it would work out how many episodes it needed to get.
This code worked for a bit
(I think,
I don't know if I was using puckfetcher daily at that point).
Eventually,
I realized this was a bad idea.
To download new podcast episodes,
puckfetcher calls down the whole RSS feed for a podcast.
This feed contains metadata on every episode ever released for a podcast,
and feedparser is nice enough to give you a list of podcast episodes ("entries").
To figure out how many podcast episodes need to be downloaded,
all that Puckfetcher really needs to do is compare how many entries there are with how many it had last time it checked,
and download the difference.
This is what it does now,
and I got to remove a lot of weird sketchy schedule-checking code that didn't work for half of my podcasts anyways.

I lost count of how many off-by-one errors I fixed while working on puckfetcher.
 They mostly stem out of a design choice I made early in the process.
In my code,
I use zero-based indexing for podcast entry lists and counts of how many podcast episodes were downloaded,
and things like that.
But,
everything I show to the user is one-based indexing.
I do this because I had (and have) this idea that some non-programmer will want to use puckfetcher,
and will be completely confused if it talks about the 0th episode of a podcast.
So,
I caused a problem for myself,
because every number that's going to go to the user has to be adjusted.
Over the course of development,
I've made a mistake converting at almost every place a conversion happens.
Eventually,
I wised up and changed all my variable names at conversion points to things like ONE_INDEXED_ENTRY_NUM,
and ZERO_INDEXED_ENTRY_NUM,
so I couldn't possibly mess it up again.
As of this writing,
I don't think I have any off-by-one errors,
but we'll see what the future holds.

With this project,
I wanted to set up a Proper Dev Process.
I wrote tests,
like a responsible developer.
I hooked my GitHub repo up to
[Travis CI](https://travis-ci.org
(free for open source projects!),
to run all of my tests whenever I pushed new code.
I also set up
[Coveralls](https://coveralls.io/github/andrewmichaud/puckfetcher?branch=master)
to test code coverage
(also free for open source)
and
[Code Climate](https://codeclimate.com/github/andrewmichaud/puckfetcher)
to check for some kinds of code smells
(again,
free for open source).
I tested locally before pushing,
but sometimes I made mistakes somewhere in the pipeline.
This became a problem early on in the dev process,
when I was trying to push a new version every time I made a change.
If I wasn't careful,
I'd push a broken version,
waste a bunch of time watching builds,
waste a version number,
and have to fix everything and push a new version.
I learned to test locally,
and to not bother pushing a new version until I had a bunch of stuff and until I had tested it thoroughly.

The best part of puckfetcher is that it's a thing I want to use.
I made it because I couldn't find a good podcast app.
I've used it daily because I need something to help me download my podcasts.
I'm motivated to keep working on it to fix bugs and to add new features.
I taught puckfetcher how to mark entries for subscriptions as downloaded or not downloaded,
and how to add items to the download queue,
because I wanted to get into the backlogs of podcasts I listen to,
without too much trouble.
I added the ability to show what podcasts puckfetcher knows about and what entries it has for each podcast because I wanted to know that both to debug puckfetcher and to use it in production.
One of the last things I taught puckfetcher was how to summarize what episodes were downloaded recently.
I did this because the only way I could figure out what podcast episodes I had downloaded after running a puckfetcher update was scrolling back up in the command line,
or checking dates on audio files.
I taught puckfetcher how to tell me what was downloaded in the current session,
so I didn't need to do that.
I also taught it to show me a longer list of "recently"-downloaded episodes for individual podcasts,
just for funsies.
<img src="{static}/media/dev/sideprojects_recently_downloaded_subscription.png" alt=""/>

### bots
puckfetcher wasn't the only thing I worked on last year.
I also made a bunch of Twitter bots.
I've wanted to make some Twitter bots for a while.
What finally inspired me to do it was [NaBoMaMo](http://nabomamo.botally.net/),
or National Bot Making Month.
This was an NaNoGenMo/NaNoWriMo to make a bunch of Twitter bots during the month of November.
I made [eight](https://dev.andrewmichaud.com).
The process of crafting those bots was a lot of fun,
and it led to different challenges than working on puckfetcher.

The best part of working on bots was the time limit imposed by NaBoMaMo.
I didn't aim for 30 bots in 30 days like some did,
but I still wanted to get as many done as I could.
There wasn't time to obsess over every detail of the code for the bots,
or to worry about every weird edge case the bot might trip over.
when I had something working well enough,
I deployed it.
I really enjoyed working under this deadline,
because there weren't any consequences of failure,
whether that meant pushing the deadline or turning out a subpar product.
Twitter bots are messy by design.
They tweet and tweet and tweet garbage,
and every once in a while you look at the output and the bot has somehow made something amazing.

I got some practice using APIs working on these bots.
I made
[two](https://twitter.com/randweather_bot)
[bots](https://twitter.com/weatherlies_bot)
using a weather API and had to learn how to use the [Open Weather Map](http://openweathermap.org)
API.
I wanted to make a bot working with video games so I learned how to use
[Giant Bomb's wonderful API](https://www.giantbomb.com/api/)
and slapped
[something](https://twitter.com/goties_bot)
together with that.
I wanted to get random cover art for
[some analysis](https://twitter.com/isthisska_bot),
so I combined the
[MusicBrainz API](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2)
with its sister project
[Cover Art Archive](https://coverartarchive.org).
These APIs were all well-enough documented that I could work out what I needed to do,
and I think working that out under the previously-noted time pressure made for some clever botmaking.

I also got to flex some different programming muscles than I use when I work professionally.
[Dirty Unix Bot](https://twitter.com/dirtyunix_bot)
uses a kind of made-up grammar to put together tweets -
I sorted words into "adjective" and "noun" based on what made sense to me,
and then told it how it was allowed to combine them.
The results aren't perfect,
but they're frequently funny and unexpected,
which is what I wanted.
Goties Bot needed lists of ten games for a certain year,
but there wasn't (as far as I could see) a good way to do that in the API.
So I hacked it together,
by finding out how many games there were for a year query,
and offsetting randomly into that (which is something the API did support).

I've been holding onto this post for about a year so I'm going to just throw it out.
All bots should be available at my
[GitHub](https://github.com/alixnovosi)
if you want to take a look.
No credentials,
you'll have to go beg Twitter for them yourselves.
Side projects are fun! Try to make some time for them,
and I think you'll be thankful you did.
