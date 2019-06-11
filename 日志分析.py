import re
import csv

#把日志转为Excrl
def zhuan():
    with open(r"C:\Users\阿苗\Desktop\u_ex190604.log",'r') as ff:
        aaz = ff.read()
    aaa = aaz.split('\n')
    for a in aaa:
        #a = '2019-06-04 04:34:36 61.181.255.157 GET /robots.txt - 80 - 124.239.251.237 Mozilla/5.0+() 404 0 121 524 98 2152'
        # 匹配日期
        try:
            datas = re.search('(\d{4}-\d{2}-\d{2})', a).group(1)
        except:
            datas = ''
        # 时间
        try:
            times = re.search('(\d{2}:\d{2}:\d{2})', a).group(1)
        except:
            times = ''
        # 主机ip
        try:
            ips = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', a).group(1)
        except:
            ips = ''
        # 请求方式
        try:
            hps = re.search('([A-Z].*)? /', a).group(1)
        except:
            hps = ''
        # URI资源，记录做为操作目标的统一资源标识符（URI），即访问的页面文件
        try:
            lujing = re.search('(/.*?) ', a).group(1)
        except:
            lujing = ''
        # URI查询，记录客户尝试执行的查询，只有动态页面需要URI查询，如果有则记录，没有则以连接符-表示。即访问网址的附带参数。
        try:
            chaxun = re.search('/.*? (.*?) ', a).group(1)
        except:
            chaxun = ''
        # 端口号
        try:
            duankou = re.search('/.*? .*? (\d*) ', a).group(1)
        except:
            duankou = ''
        # 访问ip
        try:
            fangwen = re.search('/.*? .*? \d* - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ', a).group(1)
        except:
            fangwen = ''
        # ua
        try:
            ua = re.search('/.*? .*? \d* - \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} (.*?) ', a).group(1)
        except:
            ua = ''
        # 状态码
        try:
            ztm = re.search('/.*? .*? \d* - \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} .*? (\d*) ', a).group(1)
        except:
            ztm = ''
        # 记录操作所花费的时间，单位是毫秒
        try:
            ss = re.search(' (\d*?)$', a).group(1)
        except:
            ss = ''
        # 服务器接受的字节数
        try:
            js = re.search(' (\d*?) \d*?$', a).group(1)
        except:
            js = ''
        # 服务器发送的字节数
        try:
            fs = re.search(' (\d*?) \d*? \d*?$', a).group(1)
        except:
            fs = ''
        # Win32状态，记录Windows状态代码，参照chxwei博客上前几天发的日志“IIS中的sc-win32-status——Win32状态详细说明”的说明。
        try:
            win = re.search(' (\d*?) \d*? \d*? \d*?$', a).group(1)
        except:
            win = ''
        # 协议子状态，记录HTTP子状态代码
        try:
            zzt = re.search(' (\d*?) \d*? \d*? \d*? \d*?$', a).group(1)
        except:
            zzt = ''
        with open(r"C:\Users\阿苗\Desktop\aaaaa.csv",'a',newline='') as f:
            myWriter = csv.writer(f)
            myWriter.writerow([datas, times, ips, hps, lujing, chaxun, duankou, fangwen, ua, ztm, zzt, win, fs, js, ss])

zhuan()
