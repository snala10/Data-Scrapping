# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 07:05:45 2022

@author: Sitapur
"""

import scrapy
    
class AmazonHeadphones(scrapy.Spider):
    name = 'Amazon_headphones'
    def start_requests(self):
        url='https://www.amazon.in/gp/navigation/ajax/generic.html?ajaxTemplate=hamburgerMainContent&pageType=Gateway&hmDataAjaxHint=1&navDeviceType=desktop&isSmile=0&RegionalStores%5B%5D=ctnow&isPrime=0&isBackup=false&hashCustomerAndSessionId=d15540748fd129a50c7d350e0bb42195ad894a2e&isExportMode=false&languageCode=en_IN&environmentVFI=AmazonNavigationCards%2Fdevelopment%40B6069586138-AL2_x86_64&secondLayerTreeName=amazon_echo_T1%2Bshopall_fire_tv_t2%2Bnavkindlereadersindic%2BAudibleAudiobooks%2Bamazon_prime_video%2Bamazon_prime_music%2BMobiles_Computers%2BTV_Appliances_Electronics%2Bmens_fashion%2Bwomens_fashion%2Bhome_kitchen_pets%2Bbeauty_health_grocery%2Bsports_fitness_luggage%2Btoys_baby_kids%2Bauto_industrial%2BBooks%2Bmusic_movies_games%2BGift_Cards'
        yield scrapy.Request(url=url,callback=self.get_category)
        
   

    def get_category(self, response):
        for item in response.css('ul[data-menu-id="9"] a'):
            print(item)
           


