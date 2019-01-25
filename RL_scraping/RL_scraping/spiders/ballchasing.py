# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.http import Request
from urllib.parse import urljoin
import urllib

from RL_scraping.items import RlScrapingItem
from scrapy.utils.project import get_project_settings


class BallchasingSpider(CrawlSpider):

    name = 'ballchasing'
    allowed_domains = ['ballchasing.com']
    '''
        Change start_urls when you change Ranks to be scraped.
    '''
    start_urls = ['https://ballchasing.com/?w=all&title=&player-name=&size=3v3&ranked=ranked&season=9&min-rank=16&max-rank=18&replay-after=&replay-before=&upload-after=&upload-before=']

    files = ['test.json']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h2[@class='replay-title']/a", ), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//nav/a[@class='pagination-next']", ), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if '/replay/' in response.url:
            stat_url = str(response.url) + '/stats/'
            # yield{ 'second': stat_url}
            yield Request(stat_url, callback=self.getStats)



    def getStats(self, response):
        # yield { 'second': 'yes'}
        for link in response.xpath("//following::div[1]/a[@title='Export stats as CSV']"):
            loader = ItemLoader(item=RlScrapingItem(), selector=link)
            relative_url = link.xpath("//following::div[1]/a[@title='Export stats as CSV']/@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            yield {'last': absolute_url}
            yield loader.load_item()
