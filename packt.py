from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)
browser.get("https://www.packtpub.com/free-learning")
dailyFreeBookInfo = browser.find_element_by_class_name("product__info")
print(dailyFreeBookInfo.text)

browser.close()