# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import Quote,Events


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # r_url = item['site_url']
        # record = Events(url=item['site_url'],hashed_data=item.get('hashed-data'))
        # print(record)
        # record.save()


        dup_check = Events.objects.filter(hashed_data=item['hashed-data']).count()
    
        if dup_check == 0 :     
            record = Events(url=item['site_url'],hashed_data=item.get('hashed-data'),status="Not Updated").save()
            print("nooooooooooooot")
        else:
            dup_check = Events.objects.get(hashed_data=item['hashed-data'])
            # self.db[self.collection_name].insert(item)
            print("updateeeeeeeeeeeeeee")
            update=dup_check.status="Updated"
            print(update)
            dup_check.save()
        return item
