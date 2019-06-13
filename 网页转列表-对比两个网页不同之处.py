# coding=UTF-8
import requests

#将网页转化成列表，
url = 'http://www.****.com/'
header = {'User-Agent': '***********'}
response = requests.get(url,headers=header).text
#切割字符串，转列表
a = response.split('\n')
z = []
#for 循环读取每一个字符串，删除其中的\n\t\d和空格，
for i in a:
    responses = i.strip()
    #组成新的列表
    z.append(responses)
#去除列表中的None和空字符串
c = list(filter(None, z))
print(c)

#这是对比两个网页的不同之处
a = ['<!DOCTYPE html>', '<!--[if lte IE 8 ]><html lang="zh-CN" class="ie8"> <![endif]-->']
b = ['<!DOCTYPE html>a', '<!--[if lte IE 8 ]><html lang="zh-CN" class="ie8"> <![endif]-->']
aa = set(a)
bb = set(b)
a_b = bb - aa
print(str(a_b))
