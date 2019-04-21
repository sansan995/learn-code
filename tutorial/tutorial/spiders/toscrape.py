import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'baidu'
    start_url = ['https://www.baidu.com']

    def parse(self, response):
        filename = 'baidu.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

