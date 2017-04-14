#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'torservers.net'
SITENAME = u'torservers.net blog'
SITEURL = 'https://blog.torservers.net'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'torservers'

# Feed generation is usually not desired when developing

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
PATH = 'content'

ARTICLE_URL = '{date:%Y}{date:%m}{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

STATIC_PATHS = ['images']

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

MENUITEMS = [
 ('home', 'https://www.torservers.net/'),
 ('about', 'https://www.torservers.net/about.html'),
 ('partners', 'https://www.torservers.net/partners.html'),
 ('blog', 'https://blog.torservers.net/'),
 ('wiki', 'https://www.torservers.net/wiki/'),
 ('donate', ' https://www.torservers.net/donate.html'),
 ('contact', 'https://www.torservers.net/contact.html')
]
