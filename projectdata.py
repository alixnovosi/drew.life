import copy

#import github_colors

# data on projects, and external roots (because they're needed here).
# also toy/category construction for toybox and dev pages.

GIT_ROOT = "https://github.com/alixnovosi"
ITCH_ROOT = "https://alixnovosi.itch.io"

# project definitions.
# includes both information for dev page and for toy pages.
PROJECT_GENS = {
    "markovbox": {
        "git_name": "markovbox",
        "page_name": "markovbox",
        "toy_name": "markovbox",
        "desc": "text box generating text via Markov processes",
        "long_desc": "Generates text with Markov processes, pulling from public domain works.",
        "language": "TypeScript",

        "types": ["other", "highlights", "toy"],

        "hash": "2e7d84fe92386a97b8b0",
        "has_css": True,
    },
    "sortviz": {
        "git_name": "sortviz",
        "page_name": "sortviz",
        "toy_name": "sortviz",
        "desc": "visualizer for various sort algorithms",
        "long_desc": "Visualizer for various common (and uncommon) sorting algorithms.",
        "language": "TypeScript",

        "types": ["other", "highlights", "toy"],

        "hash": "7847e61f23227a9bdd3d",
        "has_css": True,
        "has_js": True,
    },

    "drew.life": {
        "git_name": "drew.life",
        "long_desc": "Source code for this very website.",
        "language": "HTML5, SCSS/CSS3, Markdown",
        "types": ["other"],
        "lang_code": "HTML5",
    },

    "config": {
        "git_name": "config",
        "long_desc": "Dotfiles I use.",
        "language": "Various",
        "types": ["other"],
    },

    "botskeleton": {
        "short_name": "botskeleton",
        "git_name": "botskeleton",
        "long_desc": (
            "Skeleton of a Twitter/Mastodon bot, "
            "to make making the rest of these bots easier and more repeatable."
        ),
        "language": "Python 3.6",
        "types": ["other", "highlights", "bots2017"],
    },

    "sudoku": {
        "desc": "web player of sudoku puzzles",
        "git_name": "sudoku_web",
        "language": "TypeScript/VueJS",
        "lang_code": "Vue",
        "long_desc": "Web player of Sudoku puzzles.",
        "page_name": "sudoku",
        "toy_name": "sudokus",

        "types": ["other", "toy", "highlights"],

        "hash": "0c52d3ac917cdf163731",
        "has_css": True,
        "has_js": True,
    },

    "sudokugen": {
        "git_name": "sudokugen",
        "long_desc": (
            "Library to create Sudoku puzzles. Deployed at "
            "<a href=\"https://botsin.space/@sudoku_bot\">Mastodon</a>, "
            "and <a href=\"https://twitter.com/sudokugen_bot\">Twitter</a>, "
            "and posts every ~8 hours, linking to sudoku_web."
        ),
        "language": "Python 3.6",

        "types": ["other", "highlights"],
    },

    "nonogram": {
        "git_name": "nonogram_web",
        "desc": "web player of nonogram puzzles",
        "long_desc": "Web player/solution shower of nonogram puzzles.",
        "language": "TypeScript/ReactJS",
        "lang_code": "TypeScript",
        "page_name": "nonogram",
        "toy_name": "nonograms",

        "types": ["other", "toy", "highlights"],

        "hash": "0f6a41e5ae0d0425e3c4",
        "has_js": True,
    },

    "nonogen": {
        "git_name": "nonogen",
        "long_desc": (
            "Library for creating Nonogram (also called Picross) puzzles. "
            "Deployed as a bot on "
            "<a href=\"https://twitter.com/nonogram_bot\">Twitter</a>, "
            "and "
            "<a href=\"https://botsin.space/@nonogram_bot\">Mastodon</a>. "
            "Both post every ~6 hours, linking to nonogram_web. "
            f"<a href=\"{GIT_ROOT}/nonogram_bot\"> "
            "  Bot code. "
            "</a>"
        ),
        "language": "Python 3.6",

        "types": ["other"],
    },

    "puckfetcher": {
        "git_name": "puckfetcher",
        "long_desc": (
            "A simple command-line podcast downloader. "
            "Should work on Linux and OSX, "
            "Windows support possible."
        ),
        "language": "Python 3.6",

        "types": ["other"],
    },

    "boxventure": {
        "git_name": "boxventure",
        "root": ITCH_ROOT,
        "long_desc": (
            "A very simple, rough, platformer. "
            "For "
            "<a href=\"https://itch.io/jam/games-made-quick-iii\"> "
            "Games Made Quick III</a>"
        ),
        "language": "lua/Pico-8",
        "lang_code": "Lua",
        "types": ["games"],
    },

    "sudoku_bot": {
        "git_name": "sudoku_bot",
        "long_desc": "Creates sudoku puzzles every ~8 hours.",
        "language": "Python 3.6",
        "types": ["bots2019"],
    },

    "nonogram_bot": {
        "git_name": "nonogram_bot",
        "long_desc": "Creates nonogram (also known as picross) puzzles every 6 hours.",
        "language": "Python 3.6",
        "types": ["bots2017"],
    },

    "treegen_bot": {
        "git_name": "treegen_bot",
        "long_desc": "Draws trees of various colors and shapes every hour.",
        "language": "Python 3.6",
        "types": ["bots2017"],
    },

    "knowsska_bot": {
        "git_name": "knowsska_bot",
        "long_desc": "Answers isthisska_bot periodically.",
        "language": "Python 3.6",
        "types": ["bots2017"],
    },

    "dirtyunix_bot": {
        "git_name": "dirtyunix_bot",
        "long_desc": (
            "A bot combining command-line utils, "
            "in ways that sound as dirty as possible"
        ),
        "language": "Python 3.6",
        "types": ["bots2016"],
    },

    "isthisska_bot": {
        "git_name": "isthisska_bot",
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
        "long_desc": (
            "A bot lying about the weather in a random city. "
            "Pulls from same sources as randweather_bot."
        ),
        "language": "Python 3.6",
        "types": ["bots2016"],
    },

    "fantasymetro_bot": {
        "git_name": "fantasymetro_bot",
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
        "long_desc": "A bot that tells you a time zone where it isn't Happy Hour.",
        "lang_code": "Bash",
        "language": "Bash, Python 3.6",
        "types": ["bots2016"],
    },

    "haskell_bot": {
        "git_name": "haskell_bot",
        "long_desc": "A bot making jokes about functional programming and Haskell.",
        "language": "Haskell",
        "types": ["bots2016"],
    },

    "goties_bot": {
        "git_name": "goties_bot",
        "long_desc": "A bot creating Game of the Year lists for various years.",
        "language": "Python 3.6",

        "types": ["bots2016"],
    },

    "bounce": {
        "git_name": "bounce",
        "page_name": "bounce",
        "toy_name": "bounce",
        "desc": "bouncing ball in a box",
        "long_desc": "Bouncing ball in a box",
        "language": "TypeScript",

        "types": ["other", "toy"],

        "hash": "c89f08729db224899387",
        "has_js": True,
    },

    "lorenz": {
        "git_name": "lorenz",
        "page_name": "lorenz",
        "toy_name": "lorenz",
        "desc": "mini lorenz attractor with some controls",
        "long_desc": "mini lorenz attractor with some controls",
        "language": "TypeScript",

        "types": ["other", "toy"],

        "hash": "c830fe0d49bb46d23fd4",
        "has_css": True,
        "has_js": True,
    },

    "tree": {
        "git_name": "tree_web",
        "page_name": "tree",
        "toy_name": "tree",
        "desc": "tree experiment",
        "long_desc": "Tree drawing experiment.",
        "language": "TypeScript",

        "types": ["other", "toy"],

        "hash": "6c7c761c5af011afb078",
        "has_css": True,
        "has_js": True,
    },

    "JustSudoku": {
        "git_name": "JustSudoku",
        "long_desc": "Haskell command-line-only Sudoku app. No puzzle generation.",
        "language": "Haskell",
        "types": ["other"],
    },
}

PROJECTS = copy.deepcopy(PROJECT_GENS)
for key, value in PROJECT_GENS.items():

    if value.get("root", None) is None:
        value["root"] = GIT_ROOT

    value["git_url"] = f"{value['root']}/{value['git_name']}"

    if value.get("has_css", False) or value.get("has_js", False):
        url_root = f"/dist/{key}/main.{value['hash']}"

    if value.get("has_css", False):
        value["css_url"] = f"{url_root}.css"

    if value.get("has_js", False):
        value["js_url"] = f"{url_root}.js"

    if value.get("lang_code", None) is None:
        value["lang_code"] = value["language"]

    PROJECTS[key] = value

# aid for constructing JS toys page without pain.
TOYS = {
    key:value
    for (key, value) in PROJECTS.items()
    if "toy" in value.get("types", [])
}

# aid for constructing dev page without pain.
DEV_SECTIONS = ["highlights", "games", "bots2019", "bots2017", "bots2016", "other"]
DEV_TITLES = {
    "bots2016": "Twitter Bots - #NaBoMaMo 2016",
    "bots2017": "Twitter Bots - #NaBoMaMo 2017",
    "bots2019": "Twitter Bots - 2019",
    "games": "Games",
    "other": "Other",
}

DEV_ITEMS = {
    section_key:{
        key:value
        for (key, value) in PROJECTS.items()
        if section_key in value.get("types", [])
    }
    for section_key in DEV_SECTIONS
}
