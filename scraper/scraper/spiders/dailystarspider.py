import scrapy


class DailystarspiderSpider(scrapy.Spider):
    name = 'dailystarspider'
    allowed_domains = ['thedailystar.net']
    # start_urls = ['http://https://www.thedailystar.net//']
    start_urls = ['https://www.thedailystar.net/todays-news']

    def parse(self, response):
        news_categories = []
        categories = response.css('li.expanded  a::attr(href)').extract()
        for x in categories:
            a =x.split("/")
            if len(a)==2:
                news_categories.append(''.join(a[1:]))
        news_categories = news_categories[:10]
        news_categories = ['https://www.thedailystar.net/'+ x +'/' for x in news_categories]
        yield from response.follow_all(news_categories, self.news_pages)
        # yield {'news_categories':news_categories}



    def news_pages(self, response): #categories news links 
        news_links = response.css('h3.title a::attr(href)').extract()
        yield {'news_links':news_links}



    # def parse(self, response): #To days news links 
    #     news_links = response.css('td a::attr(href)').extract()
    #     news_links = ['https://www.thedailystar.net'+x for x in news_links]
    #     yield from response.follow_all(news_links, self.news_details)
    #     # yield {'news_links':news_links}

    # def news_details(self, response):
    #     headline = response.css('h1::text').extract()
    #     # headline =  ''.join(headline) or use get()
    #     date = response.css('.text-10::text').extract()
    #     images = response.css(
    #         '.section-media img::attr(data-srcset)').extract()
    #     news_1 = response.css('p strong::text').extract()
    #     news_2 = response.css('.section-content p::text').extract()
    #     news_detail = news_1 + news_2
    #     yield {'headline': headline, 'images': images, 'date': date, 'news_detail': news_detail}
