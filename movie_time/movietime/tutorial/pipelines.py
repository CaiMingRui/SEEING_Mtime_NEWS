# -*- coding: utf-8 -*-
import os
import shutil
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import spiders.tasknine

#宝猪！！！看这里！！！
#这个文件我做了处理，主要是保存路径大佬要求是电影名

import json
class MovieTimePipeline(object):
    def process_item(self, item, spider):
        if (os.path.exists("/home/caimingrui/SJWJ/movietask2/date/" +str("2017"))):#这个是判断文件夹是否存在的，如果存在就输出什么，然后如果不存在的话我就兴建一个～
            print '文件已存在'
        else:
            os.mkdir("/home/caimingrui/SJWJ/movietask2/date/" + str("2017"))#这歌就是新建一个，文件夹名字就是那个item【moviename】的内容
        filename="/home/caimingrui/SJWJ/movietask2/date/" + str("2017")+"/"+str(item['request_url'])
        with open(filename,"a")as f:
            f.write('\"moviename\":'+item['moviename']+'\n')
            f.write('\"news_id\":'+str(item['news_id'])+'\n')
            f.write('\"pub_time\":'+''.join(item['pub_time'])+'\n')
            f.write('\"cole_time\":'+item['cole_time']+'\n')
            f.write('\"language\":'+item['language']+'\n')
            # f.write('\"img_src\":'+''.join(item['img_src'])+'\n')
            f.write('\"classification\":'+''.join(item['classification'])+'\n')
            f.write('\"request_url\":'+''.join(item['request_url'])+'\n')
            f.write('\"title:\"'+''.join(item['title'])+'\n')
            f.write('\"body\":'+''.join(item['body']))
        return item