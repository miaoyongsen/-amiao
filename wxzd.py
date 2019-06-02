from __future__ import unicode_literals
import datetime
from wxpy import *
import requests
import hashlib
import time
from selenium import webdriver
from PIL import Image


bot = Bot(cache_path=True)
mdd ='60ca8d5c6f8cf11f8829905bdd96d299'

def jietu():
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\阿苗\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get("http://www.tjbh.gov.cn/")
    # 不使用这个就是手机版
    driver.maximize_window()
    time.sleep(2)
    driver.get_screenshot_as_file(r'E:\报告\aa.png')
    driver.close()
    infile = r'E:\报告\aa.png'
    outfile = r'E:\报告\aaa.png'
    im = Image.open(infile)
    (x, y) = im.size  # read image size
    x_s = 700  # define standard width
    y_s = y * x_s / x  # calc height based on standard width
    out = im.resize((int(x_s), int(y_s)), Image.ANTIALIAS)  # resize image with high-quality
    out.save(outfile)

def get_news1():
#获取网页源代码
    url = 'http://www.xxx.cn/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        response = requests.get(url,headers=header,timeout=60)
        shu = response.status_code          #状态码
        #转译中文
        response.encoding = 'utf-8'
        responses = response.text
        #加密
        md = hashlib.md5()     #构造一个MD5
        md.update(responses.encode())
        a = md.hexdigest()
        return a,shu,responses
    except:
        return None

#微信发送模块
def send_news(aa):

    try:
        my_friend = bot.friends().search(u'xx')[0]   #你朋友的微信名称，不是备注，也不是微信帐号。
        my_friends = bot.friends().search(u'xxx')[0]   #你朋友的微信名称，不是备注，也不是微信帐号。
        my_friendss = bot.friends().search(u'xxx')[0]   #你朋友的微信名称，不是备注，也不是微信帐号。

        if get_news1()[0] != aa and get_news1() != None:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            jietu()
            c = r'E:\报告\aaa.png'
            my_friend.send_image(c)
            my_friends.send_image(c)
            my_friendss.send_image(c)

            my_friends.send(u"网页被篡改，请查看网址http://www.xxx.cn/" + '\n' + 'md5值：' + get_news1()[0] + '\n' + '网页状态码：' + str(get_news1()[1]) + '\n' + '当前时间：' + nowTime)
            my_friendss.send(u"网页被篡改，请查看网址http://www.xxx.cn/" + '\n' + 'md5值：' + get_news1()[0] + '\n' + '网页状态码：' + str(get_news1()[1]) + '\n' + '当前时间：' + nowTime)
            my_friend.send(u"网页被篡改，请查看网址http://www.xxx.cn/" + '\n' + 'md5值：' + get_news1()[0] + '\n' + '网页状态码：' + str(get_news1()[1]) + '\n' + '当前时间：' + nowTime)
            global mdd
            mdd = get_news1()[0]
        elif get_news1() == None:
            my_friend.send(u'请求超时')
        else:
            print('一切正常')
    except:
        my_friend = bot.friends().search(u'xx')[0]#你的微信名称，不是微信帐号。
        my_friend.send(u"消息发送失败了")

#md5报错之后修改


if __name__ == "__main__":
    while True:
        send_news(mdd)
        #请求间隔
        time.sleep(300)
