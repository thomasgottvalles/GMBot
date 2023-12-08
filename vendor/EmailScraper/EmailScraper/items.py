import scrapy

class EmailsItems(scrapy.Item):
    contact = scrapy.Field()
    link_external = scrapy.Field()
    link_internal = scrapy.Field()
    text_external = scrapy.Field()
    text_internal = scrapy.Field()
    pass

class PageItems(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    emails = scrapy.Field()
    pass