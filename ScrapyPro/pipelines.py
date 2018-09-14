# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  requests
import os
class ScrapyproPipeline(object):
    def process_item(self, item, spider):
        f = open("qiushibaike2.txt", "a",encoding="utf-8")
        # f.write(item["title"][0])
        # print(item["title"][0])
        # for i in range(len(item["imagurl"])):
        #     imag=requests.get("https:"+item["imagurl"][i])
        #     print("https:"+item["imagurl"][i])
        #     print(imag.status_code)
        #
        #     f=open(str(i)+".jpeg","wb")
        #     f.write(imag.content)
        #     f.close()
        for i in range(len(item["author"])):
            #f = open(item["author"][i].replace('\n','')[0]+".txt", "w")
            f.write(item["url"]+"\n")
            f.write(str(i)+"  author:"+item["author"][i].replace('\n',''))
            f.write("content:"+item["content"][i].replace('\n','') + "\n")
        f.close()

        return item

