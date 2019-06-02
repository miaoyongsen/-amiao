from selenium import webdriver


driver = webdriver.PhantomJS(executable_path=r'C:\Users\阿苗\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.tjbh.gov.cn/")
#不使用这个就是手机版
#driver.maximize_window()
driver.get_screenshot_as_file(r"C:\Users\阿苗\Desktop\aaz.png")
driver.close()
