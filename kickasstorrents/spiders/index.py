# -*- coding: utf-8 -*-
import scrapy
import ast
from kickasstorrents.items import KickasstorrentsItem

class IndexSpider(scrapy.Spider):
    name = "index"
    allowed_domains = ["kickasstorrentsa.com"]
    filename = "links.txt"
    

    def __init__(self,category="movies",limit=400):
        self.category = category
        self.start_urls = []
        for i in range(1,limit):
            self.start_urls.append("http://kickasstorrentsa.com/" + self.category + "/" + str(i) +  "/")
        

    def parse(self, response):
        
        links = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]/td/div/div/a/@href').extract()
        
        magnet = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]/td/div/div/@data-sc-params').extract()
        magnets = []
        for m in magnet:
            magnets.append(ast.literal_eval(m)['magnet'])
        size = response.xpath('//*[starts-with(@class,"nobr center")]')
        l = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]')
        
        dateadded = l.xpath("td[4]/@title").extract()
        sizes = l.xpath("td[2]/text()").extract()
        byte = l.xpath("td[2]/span/text()").extract()
        seeds = l.xpath("td[5]/text()").extract()
        leechs = l.xpath("td[6]/text()").extract()
        links = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]/td/div/div/a/@href').extract()
        titles = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]/td/div/div/a/text()').extract()
        files = l.xpath("td[3]/text()").extract()
        torrents = response.xpath('//*[starts-with(@id,"torrent_' + self.category + '_torrents")]/td/div/a[4]/@href').extract()
        
        cat = response.xpath('//*[@id="cat_12528715"]/strong/a/text()').extract()
        cat = '>'.join(cat)
        for i in range(0,len(l)):
            print "-----"
            item = KickasstorrentsItem()
            item['title'] = titles[i]
            #item['category'] = cat[i]
            item['size'] = sizes[i]
            item['size'] = sizes[i]
            item['files'] = files[i]
            item['age'] = dateadded[i]
            item['seed'] = seeds[i]
            item['leech'] =leechs[i]
            item['url'] = links[i]
            item['magnet'] = magnets[i]
            item['torrent'] = torrents[i]
            item['mb'] = byte[i]
            print titles[i]
            yield item

        
