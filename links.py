# link configuration.
import os
import sys
sys.path.append(os.curdir)

from projectdata import *

# social links
SOCIAL = [
    ("github", GIT_ROOT),
    ("itch.io", ITCH_ROOT),
    ("twitch", "https://twitch.tv/alixnovosi"),
    ("youtube", "https://youtube.com/alixnovosi"),
]

# static pages
PAGES = [
    ("code stuff", "dev.html"),
    ("skills", "skills.html"),
    ("about me", "about.html"),

    ("goty2015", "goty2015.html"),
    ("goty2016", "goty2016.html"),
    ("goty2017", "goty2017.html"),
    ("goty2018", "goty2018.html"),

    ("books", "books2018.html"),
]

# pages that go into their own little zones.
# with possibly different nav
SUBPAGES = [
    ("blog", "blog/index.html"),
    ("goty", "goty2018.html"),
    ("books", "books2018.html"),
]

# index subpages, just js toys for now.
INDEX_SUBPAGES = [
    ("javascript toys", "toybox.html"),
]

TOPLEVEL_PAGES = [
    ("code stuff", "dev.html", "dev"),
    ("skills", "skills.html", "skills"),
    ("about me", "about.html", "about"),
]
