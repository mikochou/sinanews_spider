# coding=utf-8
from __future__ import absolute_import
import scrapy
import pprint
from news_scraper.items import NewsItem


class SinaSpider(scrapy.Spider):
    name = "sina"

    def start_requests(self):
        urls = [
            'https://www.sina.com.cn/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        match = ['//li/a', '//h2/a', '//h3/a']
        suffix = ['html', 'shtml', 'htm']

        data = [urls.xpath("text()""|@href").extract() for i in match
                for urls in response.xpath(i)]
        titles = [i[1] for s in suffix for i in data
                  if len(i) == 2 and len(i[1]) > 9 and s in i[0].split('.')]
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(titles)
        item = NewsItem()
        for title in titles:
            item['title'] = title
            yield item
