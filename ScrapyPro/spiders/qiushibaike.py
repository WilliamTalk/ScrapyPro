# -*- coding: utf-8 -*-
import scrapy
from ScrapyPro.items import ScrapyproItem

from scrapy.http import Request

class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['www.qiushibaike.com']
    #start_urls = ['http://www.qiushibaike.com/']
    ua = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36"}
    count=0

    def start_requests(self):

        yield Request("http://qiushibaike.com/",headers=self.ua)

    def parse(self, response):
        item = ScrapyproItem()
        item["content"] = response.xpath("//div[@class='content']/span/text()").extract()
        item["author"] = response.xpath('//div[@class="author clearfix"]/a/h2/text()').extract()
        nextpage=response.xpath('//span[@class="next"]/../@href').extract()
        yield item
        if nextpage:
          print("http://qiushibaike.com"+nextpage[0])
          self.count = self.count + 1
          print(self.count)
          yield  Request(url="https://www.qiushibaike.com"+nextpage[0],headers=self.ua,callback=self.parse)



    # def parse_nextpage(self,response):
    #    # item_1 = response.meta['item_1']
    #     item = ScrapyproItem()
    #
    #     item["content"] = response.xpath("//div[@class='content']/span/text()").extract()
    #     item["author"] = response.xpath('//div[@class="author clearfix"]/a/h2/text()').extract()
    #
    #
    #     yield  item
