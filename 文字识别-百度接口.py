from aip import AipOcr
from wxpy import *


bot = Bot(cache_path=True)
def jiekou():
    #百度关键字识别
    APP_ID = '****'
    API_KEY = '****'
    SECRET_KEY = '****'
    client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
    z = ''
    #图片源
    with open(r"C:\Users\**\Desktop\aaaa_wps图片_WPS图片.png",'rb') as f:
        img = f.read()
        msg = client.basicGeneral(img)
        for i in msg.get('words_result'):
            z = z + i.get('words')
    #返回一个识别之后的字符串
    return z

def weixin():
    #赋值
    zw = jiekou()
    my_friend = bot.friends().search(u'**')[0]  # 你朋友的微信名称，不是备注，也不是微信帐号。
    #加判断
    if '**' in zw:
        my_friend.send(u"有关键字:**")
    elif '**' in zw:
        my_friend.send(u"有关键字:**")

weixin()