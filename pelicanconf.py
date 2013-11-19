#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'torservers.net'
SITENAME = u'blog.torservers.net'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Torproject', 'https://torproject.org/'),
          )

# Social widget
SOCIAL = (('Torservers', 'https://twitter.com/torservers'),
	  ('Github', 'https://github.com/torservers'),
         )

DEFAULT_PAGINATION = False
ARTICLE_EXCLUDES = ('theme', 'output',)
THEME = "theme/tuxlite_tbs"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
