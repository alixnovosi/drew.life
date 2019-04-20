#!/usr/bin/env python3

AUTHOR = "drew"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = False

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

# blogroll
LINKS = (
    ("blog", "/blog/"),
    ("skills", "{pages}/skills.html"),
)

# social widget
SOCIAL = [
          ("github", "https://github.com/alixnovosi/"),
          ("twitter", "https://twitter.com/alixnovosi"),
          ("twitch", "https://twitch.tv/alixnovosi"),
          ("youtube", "https://youtube.com/alixnovosi"),
          ("itch.io", "https://alixnovosi.itch.io"),
]

TEMPLATE_PAGES = {
    "../theme/templates/home.html": "index.html",
}

# file location settings
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

