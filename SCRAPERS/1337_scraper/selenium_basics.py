mport os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import presence_of_element_located



from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## ORIGINAL CODE ###
# OS = os.name
# # s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
# driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
# driver.get('https://1337x.to/')



## To Load Extensions::
try:
    OS = os.name
    chrome_options = Options()
    chrome_options.add_extension('/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx')
    driver = webdriver.Chrome(options=chrome_options, executable_path= r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
    time.sleep(2)
    driver.get('https://1337x.to/')
    driver.implicitly_wait(25)  ### no need to call more than once
    print(OS)
    print(driver)
    #print(driver.text)

except Exception as e:
    print('ERROR IN PARSING CHROME EXTENSION', str(e))

try:
    search_box = driver.find_element_by_id('autocomplete')
    print(search_box.text)
    search_box.click()
    search_box.send_keys('chopper')
    click_search_box = driver.find_element_by_class_name('flaticon-search')
    #click_seach_box.click()
    #click_search_box.send_keys(Keys.ENTER)
    search_box.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("html/xxxxx").send_keys('keys.ENTER')
except Exception as e:
    print('Element not found CANNOT FIND SEARCH BOX ', str(e))


try:
    search_box01 = driver.find_element_by_id('autocomplete')
    print(search_box01.text)
    search_box01.click()
    search_box01.send_keys(Keys.CONTROL, "a")
    search_box01.clear()
    search_box01.send_keys('the titanic')
    search_box01.send_keys(Keys.ENTER)


except Exception as e:
    print('Element not found 2nd search', str(e))


### IMPLIMENT EXPLICIT WAIT
## SINCE THE WEBPAGE MAY TAKE LONG TO LOAD, AND TIME TO PARSE, SET UP AN EXPLICIT WAIT--> THIS WILL WAIT UNTIL THE DEFINED THING IS LOADED
## SET UP LOOP TO ITERATE THROUGH LIST OF ELEMENTS

try:
    body = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'table-list-wrap'))
        #EC.presence_of_all_elements_located((by.CLASS, 'table-list table table-responsive table-striped'))  ##
    )
    print(body.text)
    print(),print()
    print('1111111111')

    href_link = body.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
    print(href_link.text)

except Exception as e:
    print('Element not found body search', str(e))

try:
    click_link = driver.find_element_by_link_text('The Titanic Secret by Clive Cussler, Jack Du Brul EPUB')
    print(click_link.text)
    click_link.click()

except Exception as e:
    print('Element not found click test', str(e))

try:
  #  magnet = driver.find_element
    magnet_pull =WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))

    )
    print('magnetpull info')
    print(magnet_pull.text)
    magnet_link = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[1]/a")
    print(magnet_link.text)
    magnet_link.click()


except Exception as e:
    print('MAGNET PULL ERROR', str(e))
    driver.quit()
