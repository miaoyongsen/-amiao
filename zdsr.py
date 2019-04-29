import time
import pyautogui                        #终端输入库
from threading import Timer

def ding():
    pyautogui.click(1000, 500)          #点击像素点
    pyautogui.typewrite('mkdir a')      #创建a文件
    pyautogui.typewrite(['enter'])      #回车
    pyautogui.typewrite('cd a')         #移动到a目录
    pyautogui.typewrite(['enter'])
    print(time.time())                  #打印当前时间
while True:
    ding()
    time.sleep(5)


