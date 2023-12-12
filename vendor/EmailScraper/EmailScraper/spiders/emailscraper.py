# -*- coding: utf-8 -*-
# Exemple : scrapy crawl emailscraper -a domain=domain.com -o sortie.json
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from tldextract import extract

from EmailScraper.items import PageItems, EmailsItems

from pydispatch import dispatcher
from scrapy import signals


class EmailScraper(CrawlSpider):
    name = 'emailscraper'
    custom_settings = { 'HTTPERROR_ALLOW_ALL': True,
                        'DEPTH_LIMIT': 3,
                        'CLOSESPIDER_PAGECOUNT': 30}

    def __init__(self, domain=None, *args, **kwargs):
        self.start_urls = ['http://' + domain]
        self.target_domain = domain
        self.allowed_domains = [domain]
        self.rules = [
            Rule(
                LinkExtractor(), 
                callback='parse_page',
                follow=True)
        ]
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        dispatcher.connect(self.spider_idle, signals.spider_idle)
        super(EmailScraper, self).__init__(*args, **kwargs)
        
    def parse_page(self, response):
        url_extracted = extract(response.url)
        if self.target_domain == '{}.{}'.format(url_extracted.domain, url_extracted.suffix):
            item_page = PageItems()
            item_page['url'] = response.url
            item_page['status'] = response.status
            item_page['emails'] = self.parse_emails(response)
        yield item_page    
                
    def parse_emails(self, response):
        item_emails = EmailsItems()
        item_emails['link_internal'] = []
        item_emails['link_external'] = []
        item_emails['text_internal'] = []
        item_emails['text_external'] = []
        for link in response.xpath('//a[contains(@href, "mailto")]/@href').getall():
            link_extracted = extract(link)
            if self.target_domain == '{}.{}'.format(link_extracted.domain, link_extracted.suffix):
                item_emails['link_internal'].append(link)
            else:
                item_emails['link_external'].append(link)
        for link in response.xpath('//body').re('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'):
            link_extracted = extract(link)
            if self.target_domain == '{}.{}'.format(link_extracted.domain, link_extracted.suffix):
                item_emails['text_internal'].append(link)
            else:
                item_emails['text_external'].append(link)
        return item_emails
    
    def spider_opened(self):
        print("EmailScraper/spider_opened")
        
    def spider_idle(self):
        print("EmailScraper/spider_idle")     
    
    def spider_closed(self):
        print("EmailScraper/spider_closed")