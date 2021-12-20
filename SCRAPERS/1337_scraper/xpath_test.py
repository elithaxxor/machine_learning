import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager  ### <--- to auto install chromedrivermanager s

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


# <?xml version="1.0" encoding="UTF-8"?>
#
# <bookstore>
#
# <book category="cooking">
#   <title lang="en">Everyday Italian</title>
#   <author>Giada De Laurentiis</author>
#   <year>2005</year>
#   <price>30.00</price>
# </book>
#
# <book category="children">
#   <title lang="en">Harry Potter</title>
#   <author>J K. Rowling</author>
#   <year>2005</year>
#   <price>29.99</price>
# </book>
#
# <book category="web">
#   <title lang="en">XQuery Kick Start</title>
#   <author>James McGovern</author>
#   <author>Per Bothner</author>
#   <author>Kurt Cagle</author>
#   <author>James Linn</author>
#   <author>Vaidyanathan Nagarajan</author>
#   <year>2003</year>
#   <price>49.99</price>
# </book>
#
# <book category="web">
#   <title lang="en">Learning XML</title>
#   <author>Erik T. Ray</author>
#   <year>2003</year>
#   <price>39.95</price>
# </book>
#
# </bookstore>


# ####### CHROME OPTIONS
# start-maximized: Opens Chrome in maximize mode
# incognito: Opens Chrome in incognito mode
# headless: Opens Chrome in headless mode
# disable-extensions: Disables existing extensions on Chrome browser
# disable-popup-blocking: Disables pop-ups displayed on Chrome browser
# make-default-browser: Makes Chrome default browser
# version: Prints chrome browser version
# disable-infobars: Prevents Chrome from displaying the notification ‘Chrome is being controlled by automated software


# ChromeOptions options = new ChromeOptions()
# options.addArgument("start-maximized");
# ChromeDriver driver = new ChromeDriver(options);

# chrome_options.add_argument("--incognito")
# chrome_options = webdriver.ChromeOptions()
#  driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options, executable_path= "/Users/a-robot/PycharmProjects/pythonProject/gpu_venv")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#

#
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# driver.find_element_by_link_text(, 'itorrent')
# # download_href = WebDriverWait(driver, 15).until( EC.presence_of_element_located((By.CLASS_NAME, "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))
#


# driver = webdriver.Firefox()
# driver.get("http://www.google.com/")
#
# #open tab
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# # You can use (Keys.CONTROL + 't') on other OSs
#
# # Load a page
# driver.get('http://stackoverflow.com/')
# # Make the tests...
#
# # close the tab
# # (Keys.CONTROL + 'w') on other OSs.
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
#
#

import logging
from rich.logging import RichHandler
#
# from rich import print
# from rich import print as rprint
# from rich import pretty

from rich.console import Console
# console = Console()
#
# try:
#     do_something()
# except Exception:
#     console.print_exception(show_locals=True)
#
#



from rich.logging import RichHandler
# logging.basicConfig(
#     level="NOTSET",
#     format="%(message)s",
#     datefmt="[%X]",
#     handlers=[RichHandler(rich_tracebacks=True)]
# )
#
# log = logging.getLogger("rich")
# try:
#     print(1 / 0)
# except Exception:
#     log.exception("unable print!")

# pretty.install()
# ["Rich and pretty", True]



## ORIGINAL CODE ###
# OS = os.name
# # s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
# driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
# driver.get('https://1337x.to/')
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())



##### SETTING UP ACTION CHAIN COMMAND ###

# print('**Commencing Download Chain')
# action = ActionChains(driver)
# action.click(on_element=download_href)  # click on key
# action.send_keys(Keys.COMMAND + 't')  # send keys
# action.perform()  # execute action
# print('download_href \n', download_href.txt)
# # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# download_href_click = driver.find_element_by_link_text('http://itorrents.org/').send_keys(Keys.COMMAND + 't')


# href_link =

## absolute xpaths change overtime
# xpath = //input[@name='uid']
# name = pos, arg

### to use contains --
# xpath ='//*[contains(text(),'here)]

### contians for href_link
# xpath = '//*[contains(HREF,'')]
#
#
# ## to select all titles
# /bookstore/book/title
#
# ##Select the title of the first book
# /bookstore/book[1]/title
#
#
# ## Select all the prices
# /bookstore/book/price[text()]
#
# Select price nodes with price>35
#     / bookstore / book[price > 35] / price
#
#
# #Select title nodes with price>35
#
# /bookstore/book[price>35]/title
#
#
#
# ## load the xml document
# var xmlhttp = new XMLHttpRequest();
#
# ## to selectnode (ie )
# xmlDoc.selectNodes(xpath);


## absolute xpaths change overtime
# xpath = //input[@name='uid']
# name = pos, arg

### to use contains --
# xpath ='//*[contains(text(),'here)]

### contians for href_link
# xpath = '//*[contains(HREF,'')]



###### GOOOD CODE ######
##### TO LOOP THROUGH A LIST WHILE IN IMPLICIT WAIT
#  sm_table = body.find_element_by_class_name('"table-list table table-responsive table-striped"')
# # sm_table = body.find_element_by_class_name('coll-1 name')
#  #sm_table = body.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
#
#  for cell in sm_table:
#      href_link = cell.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
#      print(href_link.text)


## ORIGINAL CODE ###
# OS = os.name
# # s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
# driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
# driver.get('https://1337x.to/')


#################### EXPLICIT WAIT ###########################

###### USE WHEN DOWNLOAD COMPLETES ######### (23:00)
#### use when you want to wait some to for executution
## explicit wait -- waits until condition is returned true.
## driver, 30 --> how long to wait till true
#  ## use body class to find element
#  ## nest elements in a tuple
# print(f"my_element")
# WebDriverWait(driver, 30).until(
#     EC.text_to_b_present_in_element(
#         (by.CLASS_NAME, 'progress-label'),## element filtration (class name, class name vaue as a tuple
#          'complete'                      ## expected text as a string
#
#     )
#
# )



