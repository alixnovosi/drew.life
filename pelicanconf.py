#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = "drew"
DEFAULT_LANG = "en"

PATH = "content/"

SITENAME = "drewblog"
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

GIT_ROOT = "https://github.com/alixnovosi"

# social links
SOCIAL = [
          ("github", GIT_ROOT),
          ("itch.io", "https://alixnovosi.itch.io"),
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

# aid for constructing JS toys page without pain.
TOYS = {
    "nonogram": {
        "page_name": "nonogram",
        "short_name": "nonograms",
        "desc": "web player of nonogram puzzles",
        "git_url": f"{GIT_ROOT}/nonogram_web",
        "js_url": "/dist/nonogram/main.js",
    },
    "sudoku": {
        "page_name": "sudoku",
        "short_name": "sudokus",
        "desc": "web player of sudoku puzzles",
        "git_url": f"{GIT_ROOT}/sudoku_web",
        "css_url": "/dist/sudoku/main.980acdfde66cd9e96ce0.css",
        "js_url": "/dist/sudoku/main.980acdfde66cd9e96ce0.js",
    },
    "bounce": {
        "page_name": "bounce",
        "short_name": "bounce",
        "desc": "bouncing ball in a box",
        "git_url": f"{GIT_ROOT}/bounce",
        "js_url": "/dist/bounce/main.c89f08729db224899387.js",
    },
    "lorenz": {
        "page_name": "lorenz",
        "short_name": "lorenz",
        "desc": "mini lorenz attractor with some controls",
        "git_url": f"{GIT_ROOT}/lorenz",
        "css_url": "/dist/lorenz/main.458edac1c912d54c40d9.css",
        "js_url": "/dist/lorenz/main.458edac1c912d54c40d9.js",
    },
    "tree": {
        "page_name": "tree",
        "short_name": "tree",
        "desc": "tree drawer",
        "git_url": f"{GIT_ROOT}/tree_web",
        "js_url": "/dist/tree/main.6c7c761c5af011afb078.js",
    },
    "sortviz": {
        "page_name": "sortviz",
        "short_name": "sortviz",
        "desc": "visualizer for various sort algorithms",
        "git_url": f"{GIT_ROOT}/sortviz",
        "css_url": "/dist/sortviz/main.54aa025b4b14589cada9.css",
        "js_url": "/dist/sortviz/main.54aa025b4b14589cada9.js",
    },
}

# pages in main menu - done manually instead of letting Pelican help,
# because I have specific ideas about what's linked and what's "secret".
DISPLAY_PAGES_ON_MENU = False

TOPLEVEL_PAGES = [
    ("code stuff", "dev.html", "dev"),
    ("skills", "skills.html", "skills"),
    ("about me", "about.html", "about"),
]

DIRECT_TEMPLATES = ["blog_index", "category", "author", "tag", "archives"]
DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {
    "blog_index": DEFAULT_PAGINATION,
    "category": DEFAULT_PAGINATION,
    "author": DEFAULT_PAGINATION,
    "tag": DEFAULT_PAGINATION,
    "archives": 0,
}
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
RELATIVE_URLS = False
