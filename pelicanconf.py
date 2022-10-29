AUTHOR = 'James Walters'
SITENAME = 'james.walters.click'
SITESUBTITLE = "Thoughts and lessons learned along the path of software development."
SITEURL = 'https://james.walters.click'

GRAVATAR_HASH = '04574f5e4a03ae08ef293b9adc5bc2e3'

DISPLAY_PAGES_ON_MENU = False

PATH = 'content'

THEME = "themes/piccolo"

TIMEZONE = 'America/Indianapolis'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('The Grug Brained Developer', 'https://grugbrain.dev/'),)


# Social widget
SOCIAL = (('Github', 'http://github.com/iamjameswalters'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
  'extra/CNAME': {'path': 'CNAME'},
  'extra/robots.txt': {'path': 'robots.txt'},
  }
