from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im')
    time.sleep(1)

    #browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    btm1.click()

    browser.find_element_by_xpath('//div[contains(@type,"mobileOrEmail")]/div/input').send_keys('1399580060')
    browser.find_element_by_xpath('//div[contains(@type,"password")]/div/input').send_keys('test123test456')
    time.sleep(1)
    browser.find_element_by_xpath('//div/button[contains(@type,"black")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()