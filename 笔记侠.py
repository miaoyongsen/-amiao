import requests
from pyquery import PyQuery as pq
#获取xhr的动态链接
url = 'https://www.bijixia.net/api/wechat/article/list?page=1&pageSize=10'
#填写url里面的request请求
header={'Host': 'www.bijixia.net',
        'Referer': 'https://www.bijixia.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
response = requests.post(url,headers=header)       #post请求
s = []
if response.status_code == 200:
    a = response.json()                            #转换为json
    #从preview获得属性
    items = a.get('data').get('rows')              #一级一级获取
    for item in items:
        item = item.get('id')                      #想要的东西，字典形式一一对应的
        s.append(item)
else:
    print(response.status_code)

for i in s:
    urls = 'https://www.bijixia.net/#/article/detail/' + str(i)
    response = requests.get(urls,headers=header)