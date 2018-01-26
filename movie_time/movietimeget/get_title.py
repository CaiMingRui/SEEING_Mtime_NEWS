# -*- coding: utf-8 -*-

import os
import re

folder_path = "/home/caimingrui/桌面/未命名文件夹 2/movienewsdate/moviedate/2015_2"
file_list = os.listdir(folder_path)
title_box = []
i = 0
for file in file_list:
    with open("/home/caimingrui/桌面/未命名文件夹 2/movienewsdate/moviedate/2015_2/"+file,'r') as f:
        contact = f.read()
        title = re.findall("\"title:\"(.*?)\\n",contact)[0]
        if (title != "NoneNone"):
            title_box.append(title)
            i=i+1
            print str(i) + "、" + title

print i

with open('/home/caimingrui/桌面/title','w+') as w:
    for x in title_box:
        w.write(x+'\n')