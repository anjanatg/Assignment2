import scrapy


class AgentsSpider(scrapy.Spider):
    name = "agents"
    allowed_domains = ["bhhsamb.com"]
    start_urls = ["https://bhhsamb.com"]

    def parse(self, response):
        pass
