import scrapy


class DailystarSpider(scrapy.Spider):
    name = 'dailystar'
    allowed_domains = ['https://www.thedailystar.net/']
    start_urls = ['http://https://www.thedailystar.net//']

    def parse(self, response):
        pass
