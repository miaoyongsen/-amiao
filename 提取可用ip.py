import requests
import threading
import random

fileName = 'E:\ip\ip.txt'     #打开getProxy爬取下来的ip
#读取
with open(fileName,'r') as f:   #读取
    a = f.read()

books = a.split(',')           #将字符串以，隔开 形成列表
hps = []
hp = []
for i in books:
    if i[0:6] == 'HTTPS:':
        hps.append(i)          #区分https
    else:
        hp.append(i)          #区分http
url = input('请输入网址：')     #输入网址带协议
def head():
    uas = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    ]
    ua = random.choice(uas)
    ccc = {'user-agent': ua}
    return ccc

def duos(s):

    for i in range(s*50,(s+1)*50):
        proxies = {'https': hps[i]}
        header = head()
        try:
            response = requests.get(url,headers=header,proxies=proxies,timeout=10)
            print(hps[i])
            with open('./ip_k.txt', 'a') as f:
                f.write(hps[i].lower() + ',')
        except:
            print(None)
def duo(s):
    for i in range(s*50,(s+1)*50):
        proxies = {'http': hp[i]}
        header = head()
        try:
            response = requests.get(url,headers=header,proxies=proxies,timeout=10)
            print(hp[i])
            with open('./ip_k.txt', 'a') as f:
                f.write(hp[i].lower() + ',')
        except:
            print(None)



def yws():
    #https和http用两种方式
    if url.lower()[0:5] == 'https':
        print('调用https')
        for s in range(int(len(hps) / 50)):
            t = threading.Thread(target=duos, args=(s,))
            t.start()
    elif url.lower()[0:5] == 'http:':
        print('调用http')
        for s in range(int(len(hp) / 50)):
            t = threading.Thread(target=duo, args=(s,))
            t.start()

yws()