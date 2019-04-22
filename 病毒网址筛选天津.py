import requests
from lxml import etree
import threading
import re
import socket
import json

def duo(s):
    url = 'https://www.hacked.com.cn/search_country.php?var=China&page=%s' %s
    # ua
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url,headers=header,timeout=30).text
    html = etree.HTML(response)
    url_s = html.xpath('//tr/td[8]/text()')
    ip_url = 'https://open.onebox.so.com/dataApi?callback=jQuery18307981041163634246_1555554279255&type=ip&src=onebox&tpl=0&num=1&query=ip&ip=%s&url=ip&_=1555563324'

    for url in url_s[1:]:

        if xiu(url):

            iip = xiu(url)
            url_ip = ip_url %iip
            print(iip)
            try:
                response_ip = requests.get(url_ip,headers=header).text          #请求ip接口
                aa = re.compile(r'{(.*?)}', re.S)                               #提取字典
                cc = re.findall(aa, response_ip)
                a = '{' + cc[0] + '}'                                           #拼接成字典
                b = json.loads(a)

                if '天津市' in b['1']:
                    with open(r"C:\python\d\heike.txt",'a') as f:
                        f.write(url + '\n')
                    print(url)
                    return url
            except requests.exceptions.ConnectionError as fp:
                print('Error:',fp.args)

#获得ip
def xiu(a):
    if 'www.' in a:                         #有www的网址
        try:
            ti = re.compile(r'(www.*?)/',re.S)
            pu = ti.findall(a)[0]
            # 获得ip
            ips = socket.getaddrinfo(pu, None)
            ip = ips[0][4][0]
            return ip
        except:
            print(None)
    elif ':' in a:
        try:
            ti = re.compile(r'(\d.*?):',re.S)
            ip = ti.findall(a)[0]
            return ip
        except:
            print(': ip写错了')

    else:
        if not a.endswith('/'):
            a = a + '/'
        try:
            ti = r'([a-zA-Z].*?|[0-9].*?|[$-_@.&+].*?)/'
            pu = re.compile(ti, re.S)
            c = pu.findall(a)[0]
            c = 'www.' + c
            ips = socket.getaddrinfo(c, None)
            ip = ips[0][4][0]
            return ip
        except:
            print(None)


def main():
    for s in range(32):             #开十个多线程
        t = threading.Thread(target=duo, args=(s,))
        t.start()

main()