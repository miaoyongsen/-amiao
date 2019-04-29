from selenium import webdriver
import time

brow = webdriver.Chrome()           #打开谷歌
brow.get('https://www.zhihu.com/signup?next=%2F')               #输入网址
brow.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()           #点击节点
brow.find_element_by_name('username').send_keys(17602600908)                                            #选中节点，输入账号
brow.find_element_by_name('password').send_keys('*********')                                            #选中节点，输入密码
brow.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()        #点击登陆节点
time.sleep(10)
#每天第一次不会输入验证码，

brow.close()