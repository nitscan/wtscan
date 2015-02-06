# -*- coding: utf-8 -*-
#第一个python脚本，实现功能：实现对应域名title的抓取
import sys 
import re
import urllib
import socket
import time

socket.setdefaulttimeout(1)

f = open(raw_input("请输入IP或者域名列表路径及文件名:"),'r')
file = open(raw_input("请存储结果路径及文件名:"),'w+')
ports = raw_input("请要扫描的端口,例如80,8080:").split(',')
lines = f.readlines()

n=1
print f
for eachline in lines:
    each = eachline.strip()
    for port in ports:
		eachline = "http://"+each+":"+port
		print n,eachline
		
		n+=1
		try:	
			url=urllib.urlopen(eachline).read()
			title = re.compile(r"<title>(.*?)</title>|<TITLE>(.*?)</TITLE>",re.I).search(url).group(1)
		except:
			print ("[*] %s"+"无法打开..."+"\n") % eachline
			file.write(str(n-1)+":"+eachline+"无法打开..."+"\n")
			continue
		m = re.search('utf-8|UTF-8',url)
		if m:
			try:
				title = title.decode('utf-8').encode('gbk')
			except:
				pass
		print title
		file.write(str(n-1)+":"+eachline+"的title为:"+title+"\n")
f.close()
file.close()
print ("扫描结束,请看扫描结果...")
time.sleep(3)
