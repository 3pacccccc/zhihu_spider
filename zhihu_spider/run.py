# -*- coding:utf-8 -*-
__author__ = 'maruimin'

import sys

import os

from scrapy.cmdline import execute


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


execute(['scrapy', 'crawl', 'images_spider'])