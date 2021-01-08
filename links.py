# link configuration.
import os
import sys
sys.path.append(os.curdir)

from projectdata import *

# static pages
PAGES = [
    ("code", "dev.html"),
    ("skills", "skills.html"),
    ("about", "about.html"),

    ("goty2015", "goty2015.html"),
    ("goty2016", "goty2016.html"),
    ("goty2017", "goty2017.html"),
    ("goty2018", "goty2018.html"),
    ("goty2019", "goty2019.html"),
    ("goty2020", "goty2020.html"),
    ("goty2010s", "goty2010s.html"),

    ("books", "books2018.html"),
    ("books", "books2019.html"),
    ("books", "books2020.html"),
]

# social links
SOCIAL = [
    ("twitter", "https://twitter.com/alixnovosi"),
    ("github", GIT_ROOT),
    ("itch.io", ITCH_ROOT),
    ("twitch", "https://twitch.tv/alixnovosi"),
    ("youtube", "https://youtube.com/alixnovosi"),
]

# pages that go into their own little zones.
# with possibly different nav
SUBPAGES = [
    ("blog", "blog/index.html"),
    ("goty", "goty2020.html"),
    ("goty10s", "goty2010s.html"),
    ("books", "books2020.html"),
]

TOPLEVEL_PAGES = [
    ("about", "about.html", "about"),
    ("toys", "toybox.html", "toybox"),
    ("art", "ocgallery.html", "ocgallery"),
    ("code", "dev.html", "dev"),
    ("skills", "skills.html", "skills"),
]
