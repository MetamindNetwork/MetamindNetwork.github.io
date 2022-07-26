AUTHOR = 'Metamind'
SITENAME = 'Metamind'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

ARTICLE_EXCLUDES = ['templates']
TEMPLATE_PAGES = {
    'templates/homepage.html': 'index.html',
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
