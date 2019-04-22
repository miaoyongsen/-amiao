import telnetlib
import threading

with open('E:\ip\ip.txt', 'r') as f:
    ip = f.read()
with open("E:\ip\duan.txt", 'r') as fp:
    duan = fp.read()
ip = ip.split(',')
duan = duan.split(',')

def s(a):
    for i in range(a*50,(a+1)*50):
        try:
            telnetlib.Telnet(ip[i], port=duan[i], timeout=20)
            with open('E:\ip\keyi.txt','a') as fps:
                fps.write(ip[i] + ':' + duan[i] + ',')
        except:
            print('connect failed')
        else:
            print('success')

def main():
    #int(len(ip)/8)
    for a in range(8):
        t = threading.Thread(target=s,args=(a,))
        t.start()

main()