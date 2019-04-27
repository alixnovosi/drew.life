#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = "drew"
DEFAULT_LANG = "en"

PATH = "content/"

SITENAME = "drewblog"
SITEURL = ""
SLUGIFY_SOURCE = "title"

THEME = "theme"
TIMEZONE = "America/Los_Angeles"

# feed generation settings
# no feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# social links
SOCIAL = [
          ("github", "https://github.com/alixnovosi/"),
          ("itch.io", "https://alixnovosi.itch.io"),
          ("twitter", "https://twitter.com/alixnovosi"),
          ("twitch", "https://twitch.tv/alixnovosi"),
          ("youtube", "https://youtube.com/alixnovosi"),
]

# static pages
PAGES = [
    ("code stuff", f"{SITEURL}dev.html"),
    ("skills", f"{SITEURL}skills.html"),
    ("about me", f"{SITEURL}about.html"),
    ("goty2015", f"{SITEURL}goty2015.html"),
    ("goty2016", f"{SITEURL}goty2016.html"),
    ("goty2017", f"{SITEURL}goty2017.html"),
    ("goty2018", f"{SITEURL}goty2018.html"),
    ("books", f"{SITEURL}books2018.html"),
]

# pages that go into their own little zones.
# with possibly different nav
SUBPAGES = [
    ("blog", f"{SITEURL}blog/index.html"),
    ("GOTY", f"{SITEURL}goty2018.html"),
    ("books", f"{SITEURL}books2018.html"),
]

# pages in main menu - done manually instead of letting Pelican help,
# because I have specific ideas about what's linked and what's "secret".
DISPLAY_PAGES_ON_MENU = False

TOPLEVEL_PAGES = [
    ("code stuff", f"{SITEURL}/dev.html", "code"),
    ("skills", f"{SITEURL}/skills.html", "skills"),
    ("about me", f"{SITEURL}/about.html", "about"),
]

DIRECT_TEMPLATES = ["blog_index", "category", "author", "tag"]
PAGINATED_DIRECT_TEMPLATES = ["blog_index", "category", "author", "tag"]
BLOG_INDEX_SAVE_AS = "blog/index.html"

STATIC_PATHS = [
    "media",
    "extra",  # favicon and robots.txt here.
    "dist",  # javascript for nonograms
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/humans.txt": {"path": "humans.txt"},
    "extra/keybase.txt": {"path": "keybase.txt"},

    "extra/favicon.ico": {"path": "favicon.ico"},

    "dist/NonogramWeb.js": {"path": "NonogramWeb.js"},
    "dist/app.js": {"path": "app.js"},
    "dist/main.js": {"path": "main.js"},
    "dist/main.js.map": {"path": "main.js.map"},
}

TEMPLATE_PAGES = {
    "../theme/templates/home.html": "index.html",
}

# file location settings
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{identifier}.html"
PAGE_SAVE_AS = "{identifier}.html"

PLUGIN_PATHS = [
    "pelican-plugins",
]

PLUGINS = [
    "touch",
]

DELETE_OUTPUT_DIRECTORY = True

READERS = dict(html=None)
