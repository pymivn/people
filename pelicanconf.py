#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pymiers'
SITENAME = 'The PyMiers'
SITEURL = ''
THEME = 'themes/pymi'
STATIC_PATHS = ['css', 'images']
CSS_FILE = 'app.css'
PLUGIN_PATHS = ["plugins", ]
MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=monokai)', 'extra']

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'vi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

ARTICLE_URL = 'article/{slug}/'
ARTICLE_SAVE_AS = 'article/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'



# Blogroll
LINKS = (('PyMi homepage', 'https://pymi.vn/'),
         ('FAMILUG.org', 'http://www.familug.org/'),
         )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/pyfml/'),
          ('GitHub', 'https://github.com/pymivn/'),
          )

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
