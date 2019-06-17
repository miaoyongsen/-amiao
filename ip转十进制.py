import re
import xlrd

def fanwei(aa):
    p = mubiao('110.96.2.2')
    pp = int(p)
    z = aa[0].split('/')
    if int(z[0]) < pp and pp < int(z[1]):
        print('yes')

#ip转十进制
def mubiao(ip_s):
    yuan_ip = re.search('(\d+).(\d+).(\d+).(\d+)',ip_s)
    z = ''
    for i in range(1,5):
        a = yuan_ip.group(i)
        #如果是100~10的
        if int(yuan_ip.group(i)) < 100 and int(yuan_ip.group(i)) > 9:
            a = '0' + yuan_ip.group(i)
        #如果是10以下的
        if int(yuan_ip.group(i)) < 9:
            a = '00' + yuan_ip.group(i)
        z = z + a
    return z
fanwei(['110096000000/110127255255'])
def exc():
    book = xlrd.open_workbook(r"C:\Users\阿苗\Desktop\aaaaa.xls")
    sheet = book.sheet_by_name('aaaaa')
    lie = sheet.col_values(7)