#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'torservers.net'
SITENAME = u'torservers.net'
SITEURL = 'https://www.torservers.net/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'torservers'

# Feed generation is usually not desired when developing

FEED_ALL_RSS = 'feed/all.rss.xml'
CATEGORY_FEED_RSS = 'feed/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = '{date:%Y}{date:%m}{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

# Blogroll
#LINKS =  (('Torproject', 'https://torproject.org/'))

# Social widget
SOCIAL = (('Torservers', 'https://twitter.com/torservers'),
	  ('Github', 'https://github.com/torservers'),
         )

DEFAULT_PAGINATION = False
ARTICLE_EXCLUDES = ('theme', 'output',)
THEME = "theme/torservers"

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = [('home', 'https://www.torservers.net/'),('blog', 'https://blog.torservers.net/'),('wiki','http://www.torservers.net/wiki/')]
