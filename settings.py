# -*- coding: utf-8 -*-

# Scrapy settings for themeforest_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'themeforest_sample'

SPIDER_MODULES = ['themeforest_sample.spiders']
NEWSPIDER_MODULE = 'themeforest_sample.spiders'
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
DOWNLOAD_DELAY = 0.25
ITEM_PIPELINES = ['themeforest_sample.pipelines.ThemeforestPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Alo Ventures (+http://alo.ventures)'
