# Scrapy settings for legcoscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'legcoscraper'

SPIDER_MODULES = ['legcoscraper.spiders']
NEWSPIDER_MODULE = 'legcoscraper.spiders'

import os.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'legcoscraper (+http://odhk.github.io/)'

# Added as per 
# https://groups.google.com/forum/print/msg/scrapy-users/kzGHFjXywuY/O6PIhoT3thsJ
ITEM_PIPELINES = [
    'legcoscraper.files.FilesPipeline',
]
FILES_STORE = os.path.join(PROJECT_ROOT, 'datafiles')

DOWNLOADER_MIDDLEWARES = {
    # 100 is for the ordering of the middleware pipeline, not for timeout
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 100,
}
