import requests
import threading

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
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

def duos(s):
    for i in range(s*50,(s+1)*50):
        proxies = {'https': hps[i]}
        try:
            response = requests.get(url,headers=header,proxies=proxies,timeout=10)
            print(hps[i])
            with open('E:\ip\ips_k.txt', 'a') as f:
                f.write(hps[i].lower() + ',')
        except:
            print(None)
def duo(s):
    for i in range(s*50,(s+1)*50):
        proxies = {'http': hp[i]}
        try:
            response = requests.get(url,headers=header,proxies=proxies,timeout=10)
            print(hp[i])
            with open('E:\ip\ip_k.txt', 'a') as f:
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