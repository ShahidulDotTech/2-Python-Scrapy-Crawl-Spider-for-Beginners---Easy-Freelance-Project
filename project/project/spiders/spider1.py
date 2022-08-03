import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Spider1Spider(CrawlSpider):
    name = 'spider1'
    # A list of domains that the spider is allowed to crawl.
    allowed_domains = ['books.toscrape.com']
    # The starting point of the spider.
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        items = response.xpath('//h1/text()').getall()
        for i in items:
            # This class is a subclass of CrawlSpider, which is a subclass of scrapy.Spider
            yield {
                'text': items,
                'url': response.url
            }

        
