# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from newsapp.models import newsdetails

class ScraperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = newsdetails
