#-*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider
class Uav(CrawlSpider):
    name ="AI_uav"
    allowed_domians=[
        "wwww.uav.com"
    ]
    def parse(self, response):
        pass