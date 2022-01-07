# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from newsapp.models import News
from scrapy_djangoitem import DjangoItem


class ScraperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Fie
    # ld()
    django_model = News
