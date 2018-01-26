# # -*- coding: utf-8 -*-
# #宝猪！！！看这里！！！
# #这个文件是用来获得url的，因为大佬给的文件不是单纯的url
#
# import os
# import re
#
#
# list = os.listdir("/home/caimingrui/桌面/Url/")
# path = "/home/caimingrui/桌面/Url/list"
# for i in list:
#     os.mknod("/home/caimingrui/桌面/Url/"+"new"+i)
#     with open("/home/caimingrui/桌面/Url/"+"new"+i,'a') as w:
#         with open("/home/caimingrui/桌面/Url"+'/'+i) as f:
#             file = f.read().replace('\n','')
#             # print file
#             filere = re.findall('-http://movie.mtime.com/(.*?)/',file)
#             for url in filere:
#                 # print '\"http://movie.mtime.com/'+url+'/news.html\",'
#                 w.write('\"'+url+'\",')
