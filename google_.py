from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.google.ru/')

search_box=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
search_box.send_keys('купить кофемашину bork c804')
search_box.submit()
time.sleep(3)

mvideo=driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div/div[1]/a/h3')
mvideo.click()
time.sleep(10)

driver.quit