from scrapy import Spider, Selector
from stack_overflow.items import StackOverflowItem

class NewestSpider(Spider):
    name = 'newest'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions?tab=Newest/']

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="s-post-summary--content"]/h3')

        for question in questions:
            item = StackOverflowItem()
            item['description'] = question.xpath('a[@class="s-link"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class="s-link"]/@href').extract()[0]
            yield item
