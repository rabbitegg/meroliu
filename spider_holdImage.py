# -*- coding:utf-8 -*-
import os
import urllib

for i in range(5000, 5050):
	imageUrl = 'http://60.211.217.162:9001//opt/xydWeb/ArchFiles/upload/FqApiUploadFiles/authPic//' + str(i) + '//hold.jpg?time=1461941777435'
	if urllib.urlopen(imageUrl).code == 404:
		continue;
	else:
		file_path = str(i)
		fileName = str(i)
		if not os.path.exists(file_path):
			print '文件夹', file_path, '不存在，重新建立'
			os.makedirs(file_path)
		u = urllib.urlopen(imageUrl)
		data = u.read()
		f = open('./'+file_path+ '//'+fileName + 'IDCard_HOLD.jpg', 'wb')
		f.write(data)
		print u"正在保存图片", fileName
		f.close()

