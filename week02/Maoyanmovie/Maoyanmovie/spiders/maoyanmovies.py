# -*- coding: utf-8 -*-
import scrapy
from Maoyanmovie.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanmoviesSpider(scrapy.Spider):
    #定义爬虫名称
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com']
    #起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    #解析函数
    def parse(self,response):
        try:
            for selector in response.xpath('//div[@class="movie-hover-info"]')[:10]:
                print(selector)
                item = MaoyanItem()
                item['movie_name'] = selector.xpath("./div[1]/span[1]/text()").extract_first()
                item['movie_type'] = selector.xpath("./div[2]/text()[2]").extract_first().strip()
                item['movie_time'] = selector.xpath("./div[4]/text()[2]").extract_first().strip()
                yield item
        except Exception as e:
            print(e)