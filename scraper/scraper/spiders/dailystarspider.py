import scrapy


class DailystarspiderSpider(scrapy.Spider):
    name = 'dailystarspider'
    allowed_domains = ['https://www.thedailystar.net/']
    # start_urls = ['http://https://www.thedailystar.net//']
    start_urls = ['https://www.thedailystar.net/health/disease/coronavirus/news/omicron-surge-schools-colleges-declared-closed-indias-west-bengal-2930741']

    def parse(self, response):
        headline = response.css('h1::text').get()
        date = response.css('.text-10::text').get()
        images = response.css('.section-media img::attr(data-srcset)').extract()
        news_1 = response.css('p strong::text').extract()
        news_2 = response.css('.section-content p::text').extract()
        news_detail = news_1 + news_2
        yield {'headline':headline, 'images':images, 'date':date, 'news_detail':news_detail}