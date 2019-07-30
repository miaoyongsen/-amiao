from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import time

def huoquurl():
    #通过百度查找
    url = 'https://www.baidu.com/'
    #无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #调用chrome浏览器
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #请求百度
    driver.get(url)
    #点击节点输入
    driver.find_element_by_name('wd').send_keys('http://www.xxxx.com')                                            #选中节点，输入账号
    driver.find_element_by_id('su').click()
    # 等待10微秒，强势点击节点
    wait = ui.WebDriverWait(driver,10)
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="1"]/h3/a')).click()
    #休息3s，等待网页加载
    time.sleep(5)
    #获取倒数第一个网页，也就是新跳转出来的
    driver.switch_to.window(driver.window_handles[-1])
    #打印当前url
    return driver.current_url


if __name__ == '__main__':
    huoquurl()