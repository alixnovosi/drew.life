#!/usr/bin/env python3

AUTHOR = "drew"
DEFAULT_LANG = "en"

PATH = "content/"

# uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITENAME = "drewblog"
SITEURL = ""
# SITEURL = "https://blog.drew.life"
SLUGIFY_SOURCE = "title"

THEME = "theme"
TIMEZONE = "America/Los_Angeles"

# feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# social links
SOCIAL = [
          ("github", "https://github.com/alixnovosi/"),
          ("twitter", "https://twitter.com/alixnovosi"),
          ("twitch", "https://twitch.tv/alixnovosi"),
          ("youtube", "https://youtube.com/alixnovosi"),
          ("itch.io", "https://alixnovosi.itch.io"),
]

# static pages (that aren't "secret")
PAGES = [
    ("code stuff", "dev.html"),
    ("skills", "skills.html"),
    ("about me", "about.html"),
    ("goty2015", "goty2015.html"),
    ("goty2016", "goty2016.html"),
    ("goty2017", "goty2017.html"),
    ("goty2018", "goty2018.html"),
]

TOPLEVEL_PAGES = [
    ("blog", "blog"),
    ("code stuff", "dev.html"),
    ("skills", "skills.html"),
    ("about me", "about.html"),
]

STATIC_PATHS = [
    "media",
    "extra",  # favicon and robots.txt here.
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/humans.txt": {"path": "humans.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

TEMPLATE_PAGES = {
    "../theme/templates/home.html": "index.html",
}

DISPLAY_PAGES_ON_MENU = False

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
