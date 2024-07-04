# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AgentsSpider(scrapy.Item):
    name = 'agents'
    allowed_domains = ['bhhsamb.com']
    start_urls = ['https://www.bhhsamb.com/agents']

    def parse(self, response):
        agent_urls = response.css('.agent-name a::attr(href)').extract()
        for url in agent_urls:
            yield response.follow(url, self.parse_agent)


        next_page = response.css('.pagination-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_agent(self, response):

        yield {
            'name': response.css('h1.agent-name::text').get(),
            'phone': response.css('span.agent-phone::text').get(),
            'email': response.css('span.agent-email a::text').get(),
            'address': response.css('span.agent-address::text').get(),
        }