# -*- coding: utf-8 -*-
# import scrapy


# class ToScrapeCSSSpider(scrapy.Spider):
#     name = "toscrape-css"
#     start_urls = [
#         'http://quotes.toscrape.com/',
#     ]

#     def parse(self, response):
#         for quote in response.css("div.quote"):
#             yield {
#                 'text': quote.css("span.text::text").extract_first(),
#                 'author': quote.css("small.author::text").extract_first(),
#                 'tags': quote.css("div.tags > a.tag::text").extract()
#             }

#         next_page_url = response.css("li.next > a::attr(href)").extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))

import scrapy
import datetime
import logging
import hashlib
import os
os.environ['PYTHONHASHSEED'] = '0'
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    allowed_domains = ['tie.org']
    start_urls = ['https://www.opensv.org/','https://www.meetup.com/','https://www.eventbrite.com/','https://tie.org/']
  
    def parse(self, response):
    
        # a =['first','second']
        # title = response.xpath("//div[contains(@class,'vc_col-sm-12  wpb_column vc_column_container')]/div/div/div/div/h2/a/strong/text()").getall()
        # venue = response.xpath("//div[contains(@class,'vc_col-sm-12  wpb_column vc_column_container')]/div/div/div/div/p[1]/text()").getall()
        # links = response.xpath("//div[contains(@class,'vc_col-sm-12  wpb_column vc_column_container')]/div/div/div/div/h2/a")
        # for link in links:
        #     name = link.xpath(".//text()").get()
        #     link = link.xpath(".//@href").get()

        #     yield {
        #         'link' : link,
        #         'name': name,
        #     }
        # self.logger.info('A response from %s just arrived!', response.url)
        entire_body = response.xpath("//body/*[not(self::script)]").get()
        def remove(string):
            return string.replace(" ", "") 
        
        # logging.info(a[c])
        # c = c+1
        # logging.info(entire_body)
        
        #generate hash256 of the site data
        unspaced_output = remove(entire_body) 
        encoded_data = unspaced_output.encode()
        hashed_data = hashlib.sha256(encoded_data).hexdigest()
        # hashed_data = hash(unspaced_output)
        url =response.url
        stored_time = datetime.datetime.now().strftime("%d %B, %Y")
        yield {
            'hashed-data': hashed_data,
            'site_url':url,
            'last_visit_Date': stored_time

            }

