AUTHOR = 'Patrick Harrison'
SITENAME = 'PATRICK HARRISON'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Canada/Mountain'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ["images", "pdfs"]

# URL Settings
ARTICLE_URL = "portfolio/{slug}"
ARTICLE_SAVE_AS = "portfolio/{slug}/index.html"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican.plugins.pagination"]

THEME = "C:/Users/patrick/BGIS/COMM415/Assignment/pelican-themes/cebong"

# # Blogroll
# LINKS = (("Pelican", "https://getpelican.com/"),
#          ("Python.org", "https://www.python.org/"),
#          ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#          ("You can modify those links in your config file", "#"),)
#
# # Social widget
SOCIAL = (("Email", "mailto:patrickgharrison@outlook.com"),
          ("Github", "https://github.com/PatHarrison"),
          ("LinkedIn", "https://linkedin.com/in/patrickharri/"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
