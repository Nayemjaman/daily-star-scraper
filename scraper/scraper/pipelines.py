# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from scraper.scraper.items import ScraperItem


class ScraperPipeline(object):
    def process_item(self, item, spider):
        # if isinstance(item, ScraperItem):
        #     item.save()
        return item
        # if item not in item:
            # item.save()

