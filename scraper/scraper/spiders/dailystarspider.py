import scrapy


class DailystarspiderSpider(scrapy.Spider):
    name = 'dailystarspider'
    allowed_domains = ['https://www.thedailystar.net/']
    start_urls = ['http://https://www.thedailystar.net//']

    def parse(self, response):
        pass
