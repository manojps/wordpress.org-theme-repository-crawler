from scrapy import signals
from scrapy.exceptions import DropItem
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


##class ThemeforestSamplePipeline(object):
##    def process_item(self, item, spider):
##        return item

from scrapy import log  
#from scrapy.core.exceptions import DropItem  
from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
from scrapy.contrib.pipeline.images import ImagesPipeline  
import time  
import psycopg2 

  
  
class ThemeforestPipeline(object):  
  
    def __init__(self):  
        self.conn = psycopg2.connect("dbname='gplay' user='postgres' host='localhost' password='tjv375'")
        self.links_seen = []
    def process_item(self, item, spider):  
          
##        query = self.dbpool.runInteraction(self._conditional_insert, item)  
##        query.addErrback(self.handle_error)
        
            
        if item['link'] in self.links_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.links_seen.append(item['link'])
        cur = self.conn.cursor()
        cur.execute("insert into item (name) values (%s)", (item['link']))
        self.conn.commit()
        return item  
    
##    def _conditional_insert(self, tx, item):  
##        if item.get('name'):  
##            tx.execute(\  
##                "insert into book (name, publisher, publish_date, price ) \  
##                 values (%s, %s, %s, %s)",  
##                (item['name'],  item['publisher'], item['publish_date'],   
##                item['price'])  
##            )  
