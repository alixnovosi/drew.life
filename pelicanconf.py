#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "drew"
SITENAME = "drewblog"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
          ("github", "https://github.com/alixnovosi/"),
          ("twitter", "https://twitter.com/alixnovosi"),
          ("twitch", "https://twitch.tv/alixnovosi"),
          ("youtube", "https://youtube.com/alixnovosi"),
          )

DEFAULT_PAGINATION = False
PATH = "content/"
# SITEURL = "https://blog.drew.life"
SLUGIFY_SOURCE = "title"

THEME = "theme"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
