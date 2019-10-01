#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# TODO split this config into more files?

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

# social links
GIT_ROOT = "https://github.com/alixnovosi"
ITCH_ROOT = "https://alixnovosi.itch.io"
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

# project definitions.
# includes both information for dev page and for toy pages.
# TODO find a clean way to do self-reference.
PROJECTS = {
    "drew.life": {
        "git_name": "drew.life",
        "git_url": f"{GIT_ROOT}/drew.life",
        "long_desc": "Source code for this very website.",
        "language": "HTML5, SCSS/CSS3, Markdown",

        "types": ["other"],
    },

    "config": {
        "git_name": "config",
        "git_url": f"{GIT_ROOT}/config",
        "long_desc": "Dotfiles I use.",
        "language": "Various",

        "types": ["other"],
    },

    "botskeleton": {
        "short_name": "botskeleton",
        "git_name": "botskeleton",
        "git_url": f"{GIT_ROOT}/botskeleton",
        "long_desc": (
            "Skeleton of a Twitter/Mastodon bot, "
            "to make making the rest of these bots easier and more repeatable."
        ),
        "language": "Python 3.6",

        "types": ["other", "highlights", "bots2017"],
    },

    "sudoku": {
        "desc": "web player of sudoku puzzles",
        "long_desc": "Web player of Sudoku puzzles.",
        "git_name": "sudoku_web",
        "git_url": f"{GIT_ROOT}/sudoku_web",
        "language": "TypeScript/VueJS",

        "types": ["other", "toy", "highlights"],

        "css_url": "/dist/sudoku/main.980acdfde66cd9e96ce0.css",
        "js_url": "/dist/sudoku/main.980acdfde66cd9e96ce0.js",
        "page_name": "sudoku",
        "toy_name": "sudokus",
    },

    "sudokugen": {
        "git_name": "sudokugen",
        "git_url": f"{GIT_ROOT}/sudokugen",
        "long_desc": (
            "Library to create Sudoku puzzles. Deployed at "
            "<a href=\"https://botsin.space/@sudoku_bot\">Mastodon</a>, "
            "and <a href=\"https://twitter.com/sudokugen_bot\">Twitter</a>, "
            "and posts every ~8 hours, linking to sudoku_web."
        ),
        "language": "Python 3.6",

        "types": ["other", "highlights"],
    },

    # TODO put nonogram on the same pattern as everything else,
    # so we can just have a hash var and then yes css and yes js, or something.
    "nonogram": {
        "git_name": "nonogram_web",
        "git_url": f"{GIT_ROOT}/nonogram_web",
        "desc": "web player of nonogram puzzles",
        "long_desc": "Web player/solution shower of nonogram puzzles.",
        "language": "TypeScript/ReactJS",

        "types": ["other", "toy", "highlights"],

        "js_url": "/dist/nonogram/main.js",
        "page_name": "nonogram",
        "toy_name": "nonograms",
    },

    "nonogen": {
        "git_name": "nonogen",
        "git_url": f"{GIT_ROOT}/nonogen",
        "long_desc": (
            "Library for creating Nonogram (also called Picross) puzzles. "
            "Deployed as a bot on "
            "<a href=\"https://twitter.com/nonogram_bot\">Twitter</a>, "
            "and "
            "<a href=\"https://botsin.space/@nonogram_bot\">Mastodon</a>. "
            "Both post every ~6 hours, linking to nonogram_web. "
            "<a href=\"https://github.com/alixnovosi/nonogram_bot\"> "
            "  Bot code. "
            "</a>"
        ),
        "language": "Python 3.6",

        "types": ["other", "highlights"],
    },

    "puckfetcher": {
        "git_name": "puckfetcher",
        "git_url": f"{GIT_ROOT}/puckfetcher",
        "long_desc": (
            "A simple command-line podcast downloader. "
            "Should work on Linux and OSX, "
            "Windows support possible."
        ),
        "language": "Python 3.6",

        "types": ["other", "highlights"],
    },

    "boxventure": {
        "git_name": "boxventure",
        "git_url": f"{ITCH_ROOT}/boxventure",
        "long_desc": (
            "A very simple, rough, platformer. "
            "For "
            "<a href=\"https://itch.io/jam/games-made-quick-iii\"> "
            "Games Made Quick III</a>"
        ),
        "language": "lua/Pico-8",

        "types": ["games"],
    },

    "sudoku_bot": {
        "git_name": "sudoku_bot",
        "git_url": f"{GIT_ROOT}/sudoku_bot",
        "long_desc": "Creates sudoku puzzles every ~8 hours.",
        "language": "Python 3.6",

        "types": ["bots2019"],
    },

    "nonogram_bot": {
        "git_name": "nonogram_bot",
        "git_url": f"{GIT_ROOT}/nonogram_bot",
        "long_desc": "Creates nonogram (also known as picross) puzzles every 6 hours.",
        "language": "Python 3.6",

        "types": ["bots2017"],
    },

    "treegen_bot": {
        "git_name": "treegen_bot",
        "git_url": f"{GIT_ROOT}/tree_bot",
        "long_desc": "Draws trees of various colors and shapes every hour.",
        "language": "Python 3.6",

        "types": ["bots2017"],
    },

    "knowsska_bot": {
        "git_name": "knowsska_bot",
        "git_url": f"{GIT_ROOT}/knowsska_bot",
        "long_desc": "Answers isthisska_bot periodically.",
        "language": "Python 3.6",

        "types": ["bots2017"],
    },

    "dirtyunix_bot": {
        "git_name": "dirtyunix_bot",
        "git_url": f"{GIT_ROOT}/dirtyunix_bot",
        "long_desc": (
            "A bot combining command-line utils, "
            "in ways that sound as dirty as possible"
        ),
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "isthisska_bot": {
        "git_name": "isthisska_bot",
        "git_url": f"{GIT_ROOT}/isthisska_bot",
        "long_desc": (
            "A bot pulling random album art from "
            "<a href=\"https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2\">"
            "MusicBrainz"
            "</a> "
            "and asking if it's ska."
        ),
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "randweather_bot": {
        "git_name": "randweather_bot",
        "git_url": f"{GIT_ROOT}/randweather_bot",
        "long_desc": (
            "A bot describing the weather in a random city. "
            "Pulls from <a href=\"https://openweathermap.org/\">"
            "Open Weather Map</a> "
            "and a manually-created zip code list."
        ),
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "weatherlies_bot": {
        "git_name": "weatherlies_bot",
        "git_url": f"{GIT_ROOT}/weatherlies_bot",
        "long_desc": (
            "A bot lying about the weather in a random city. "
            "Pulls from same sources as randweather_bot."
        ),
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "fantasymetro_bot": {
        "git_name": "fantasymetro_bot",
        "git_url": f"{GIT_ROOT}/fantasymetro_bot",
        "long_desc": (
            "A bot generating plausible, "
            "but imaginary, "
            "metro systems for cities. "
            "Needs a lot of manual work to generate for a "
            "given city, unfortunately."
        ),
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "not5oclock_bot": {
        "git_name": "not5oclock_bot",
        "git_url": f"{GIT_ROOT}/not5oclock_bot",
        "long_desc": "A bot that tells you a time zone where it isn't Happy Hour.",
        "language": "Bash, Python 3.6",

        "types": ["bots2016"],
    },

    "haskell_bot": {
        "git_name": "haskell_bot",
        "git_url": f"{GIT_ROOT}/haskell_bot",
        "long_desc": "A bot making jokes about functional programming and Haskell.",
        "language": "Haskell",

        "types": ["bots2016"],
    },

    "goties_bot": {
        "git_name": "goties_bot",
        "git_url": f"{GIT_ROOT}/goties_bot",
        "long_desc": "A bot creating Game of the Year lists for various years.",
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "bounce": {
        "git_name": "bounce",
        "git_url": f"{GIT_ROOT}/bounce",
        "page_name": "bounce",
        "toy_name": "bounce",
        "desc": "bouncing ball in a box",
        "long_desc": "Bouncing ball in a box",
        "language": "TypeScript/ReactJS",

        "types": ["other", "toy"],

        "js_url": "/dist/bounce/main.c89f08729db224899387.js",
    },

    "lorenz": {
        "git_name": "lorenz",
        "git_url": f"{GIT_ROOT}/lorenz",
        "page_name": "lorenz",
        "toy_name": "lorenz",
        "desc": "mini lorenz attractor with some controls",
        "long_desc": "mini lorenz attractor with some controls",
        "language": "TypeScript/ReactJS",

        "types": ["other", "toy"],

        "css_url": "/dist/lorenz/main.458edac1c912d54c40d9.css",
        "js_url": "/dist/lorenz/main.458edac1c912d54c40d9.js",
    },

    "tree": {
        "git_name": "tree_web",
        "git_url": f"{GIT_ROOT}/tree_web",
        "page_name": "tree",
        "toy_name": "tree",
        "desc": "tree drawer",
        "long_desc": "Tree drawing experiment.",
        "language": "TypeScript/ReactJS",

        "types": ["other", "toy"],

        "js_url": "/dist/tree/main.6c7c761c5af011afb078.js",
    },

    "sortviz": {
        "git_name": "sortviz",
        "git_url": f"{GIT_ROOT}/sortviz",
        "page_name": "sortviz",
        "toy_name": "sortviz",
        "desc": "visualizer for various sort algorithms",
        "long_desc": "Visualizer for various common (and uncommon) sorting algorithms.",
        "language": "TypeScript/ReactJS",

        "types": ["other", "toy"],

        "css_url": "/dist/sortviz/main.4c1f701f657dfee6eeec.css",
        "js_url": "/dist/sortviz/main.4c1f701f657dfee6eeec.js",
    },

    "JustSudoku": {
        "git_name": "JustSudoku",
        "git_url": f"{GIT_ROOT}/JustSudoku",
        "long_desc": "Haskell command-line-only Sudoku app. No puzzle generation.",
        "language": "Haskell",

        "types": ["other"],
    },
}

# aid for constructing JS toys page without pain.
TOYS = {
    key:value
    for (key, value) in PROJECTS.items()
    if "toy" in value.get("types", [])
}

# aid for constructing dev page without pain.
DEV_SECTIONS = ["bots2016", "bots2017", "bots2019", "highlights", "games", "other"]
DEV_ITEMS = {
    section_key:{
        key:value
        for (key, value) in PROJECTS.items()
        if section_key in value.get("types", [])
    }
    for section_key in DEV_SECTIONS
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
