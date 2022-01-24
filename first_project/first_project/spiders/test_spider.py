# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 01:08:11 2022

@author: Sitapur
"""
import scrapy
from first_project.items import AuthorItems
import logging
#logging.basicConfig(filename='Mylog.log', encoding='utf-8', level=logging.DEBUG)
"""
class QuotesSpider(scrapy.Spider):
    name = 'Author'
    def start_requests(self):
        url='https://quotes.toscrape.com/'
        yield scrapy.Request(url=url,callback=self.parse)
        
   

    def parse(self, response):
        
        for div in response.css('div.quote'):
            #print(div.css('span.text::text').get())
            #print(div.css('small.author::text').get())
            yield {
                'quote':div.css('span.text::text').get(),
               'author':div.css('small.author::text').get(),
               'author_url':response.urljoin(div.css('.author+a::attr(href)').get())
               } 
            author_url=response.urljoin(div.css('.author+a::attr(href)').get())
            yield scrapy.Request(url=author_url,callback=self.author)
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
    
       
    def author(self,response):
        yield {
            
            'dob':response.css('span.author-born-date::text').get(default='not present')
            }
  """      

class QuotesSpider1(scrapy.Spider):
    name = 'Author1'
    def start_requests(self):
        url='https://quotes.toscrape.com/'
        yield scrapy.Request(url=url,callback=self.parse)
        
   

    def parse(self, response):
        
        for div in response.css('div.quote'):
            #print(div.css('span.text::text').get())
            #print(div.css('small.author::text').get())
            data= {
                'quote':div.css('span.text::text').get(),
               'author':div.css('small.author::text').get(),
               'author_url':response.urljoin(div.css('.author+a::attr(href)').get())
               } 
            author_url=response.urljoin(div.css('.author+a::attr(href)').get())
            author_request=scrapy.Request(url=author_url,callback=self.author,cb_kwargs=data)
            #author_request.cb_kwargs=data
            self.logger.info("PROceesed author "+str(data['author']))
            yield author_request
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
    
    
    
    def author(self,response,quote,author,author_url):
        """yield {
            'quote':quote,'author':author,'author_url':author_url,
            
            'dob':response.css('span.author-born-date::text').get(default='not present')
            }
        """
        output=AuthorItems()
        output['quote']=quote
        output['author']=author
        output['author_url']=author_url
        output['dob']=response.css('span.author-born-date::text').get(default='not present')
        yield output
        
    
    
            
            
            
                  
    
        