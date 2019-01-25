# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.http import Request
from urllib.parse import urljoin

from RL_scraping.items import RlScrapingItem


class BallchasingSpider(CrawlSpider):
    name = 'ballchasing'
    allowed_domains = ['ballchasing.com']
    '''
        Change start_urls when you change Ranks to be scraped.
    '''
    start_urls = ['https://ballchasing.com/?w=all&title=&player-name=&size=3v3&ranked=ranked&season=9&min-rank=16&max-rank=18&replay-after=&replay-before=&upload-after=&upload-before=']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h2[@class='replay-title']/a", ), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//nav/a[@class='pagination-next']", ), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        stat_url = response.urljoin('/stats')
        yield Request(stat_url, callback=self.getStats)
        # yield {
        #     'crawled': response
        # }


    def getStats(self, response):
        # loader = ItemLoader(item=RlScrapingItem(), selector="/html/body/section[3]/div/div[1]/div[2]/div[1]/a")
        # relative_url = response.xpath("/html/body/section[3]/div/div[1]/div[2]/div[1]/a").extract_first()
        # absolute_url = response.urljoin(relative_url)
        # loader.add_value('file_urls', absolute_url)
        # yield loader.load_item()
        