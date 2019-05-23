from xlwt import *
import xlrd
import csv

#输出目录
book_s = xlrd.open_workbook(r"C:\Users\阿苗\Desktop\工作\滨海新区备案信息.xlsx")            #目标目录
sheet_s = book_s.sheet_by_name(u'Sheet1')   #表
lie_s = sheet_s.col_values(31)              #网站域名




#返回一个网址
def bendi():
    book = xlrd.open_workbook(r"C:\Users\阿苗\Desktop\表格.xlsx")       #打开本地目录
    sheet = book.sheet_by_name(u'滨海')   #表
    lie = sheet.col_values(1)               #目标url
    biao = []                #空列表用来装目标url
    del lie[0]               #删除第一个标题
    for i in lie:
        c = i[7:]               #截取成www.xxxx.com
        biao.append(c)
    return biao

#所有信息
def fanhui(g):
    hang = sheet_s.row_values(g)        #找到的所有信息
    name = hang[20]                     #公司名字
    adds = hang[22]                     #地址
    shouji = hang[4]                    #手机号
    beian = hang[7]                     #备案信息
    #写入csv
    with open(r"C:\Users\阿苗\Desktop\ziliao.csv", 'a',newline='') as f:
        myWriter = csv.writer(f)
        myWriter.writerow([name, adds,shouji,beian,])

#主程序
def cha():
    for i in bendi():
        try:
            g = lie_s.index(i)      #获得字符串在列表中的位置
            fanhui(g)
        except:
            print(None)

if __name__ == '__main__':
    cha()