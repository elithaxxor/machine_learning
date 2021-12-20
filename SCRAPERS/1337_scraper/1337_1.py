import os
import time
import traceback
import sys
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
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.utils import ChromeType



counter00 = 0
Parsing = True
while Parsing:
    class Colors:
        reset = "\033[0m"

        # Black
        fgBlack = "\033[30m"
        fgBrightBlack = "\033[30;1m"
        bgBlack = "\033[40m"
        bgBrightBlack = "\033[40;1m"

        # Red
        fgRed = "\033[31m"
        fgBrightRed = "\033[31;1m"
        bgRed = "\033[41m"
        bgBrightRed = "\033[41;1m"

        # Green
        fgGreen = "\033[32m"
        fgBrightGreen = "\033[32;1m"
        bgGreen = "\033[42m"
        bgBrightGreen = "\033[42;1m"

        # Yellow
        fgYellow = "\033[33m"
        fgBrightYellow = "\033[33;1m"
        bgYellow = "\033[43m"
        bgBrightYellow = "\033[43;1m"

        # Blue
        fgBlue = "\033[34m"
        fgBrightBlue = "\033[34;1m"
        bgBlue = "\033[44m"
        bgBrightBlue = "\033[44;1m"
        # Magenta
        fgMagenta = "\033[35m"
        fgBrightMagenta = "\033[35;1m"
        bgMagenta = "\033[45m"
        bgBrightMagenta = "\033[45;1m"
        # Cyan
        fgCyan = "\033[36m"
        fgBrightCyan = "\033[36;1m"
        bgCyan = "\033[46m"
        bgBrightCyan = "\033[46;1m"
        # White
        fgWhite = "\033[37m"
        fgBrightWhite = "\033[37;1m"
        bgWhite = "\033[47m"
        bgBrightWhite = "\033[47;1m"
    ###########
    color = Colors()
    yellow = color.fgYellow
    red = color.fgRed
    blue = color.fgBlue
    bblue = color.fgBrightBlue
    cyan = color.fgCyan
    bg_background = color.bgBlack
    reset = color.reset


    class TorrentParser():
        def __init__(self):
            self.self = self
            self.cwd = os.getcwd()

        def get_download_len(self):
            self.torrent_list_len = len(open('hrefdata.txt').readlines())
            global list_len
            list_len = self.torrent_list_len
            print(f'**Calculating List Len in \n[{self.cwd}]')
            time.sleep(1)
            print(f'List  Len  {self.torrent_list_len}')

            return self.torrent_list_len

        @staticmethod
        def list_iterator():
            try:
                torrent_list = []
                #count = 0
               # if count00 != 0:
                hrefdata = 'hrefdata.txt'
                cwd = os.getcwd()
                href_loc = str(cwd) + f'/{hrefdata}'
                href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
                print(href_str)

                with open(href_loc) as f:
                    count = 0
                    for href in open(href_loc):
                        torrent_list = f.readlines(count)
                        website_list = [x.strip() for x in href]
                        print('website list', website_list)
                        print('torrent list ', torrent_list)
                        index = 0
                        count = count + 1
                        if count > 0:
                            total_count = count + 1
                        for iterate in torrent_list:
                            if index < count:
                                torrent_list.append(iterate)
                                print(f'[SYS]** ADDED #[{count}] \n {iterate}')
                                print(f'[SYS]** TOTAL ADDED #[{total_count}] \n {torrent_list}')
                                return iterate
                            else:
                                break
                        print(f'[SYSTEM] Found {count} items in .txt')
            except Exception as e:
                traceback.print_exc()
                print(f"{red}**[ERROR IN DICT READER]{reset}\n {str(e)}")
                sys.exit(1)

    try:
        parser = TorrentParser()
        list_len = parser.get_download_len()
        if counter00 == int(list_len):
            print('EOL--> SYS.EXIT')
            Parsing = False
            sys.exit(0)

        first_run = True
        while first_run:
            if counter00 != 0:
                first_run = False
                pass
            elif counter00 == 0:
                OS = os.name
                # chrome_options = Options()
                chrome_options = ChromeOptions()
                chrome_options = Options()
                chrome_options.add_extension("/Users/a-robot/PycharmProjects/pythonProject/gpu_venv/ad_blocker.crx")
                executable_path = r"/Users/a-robot/PycharmProjects/pythonProject/gpu_venv"
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
                #  driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
                if driver:
                    print('Driver Succesfully Installed')
                    time.sleep(2)
                    driver.get('https://1337x.to/')
                    driver.implicitly_wait(25)  ### no need to call more than once
                    print(driver)
                    print(OS)
                    print(f'**Total List Len [{list_len}]')
                    time.sleep(4)
                try:
                    print('starting test before real run.')
                    time.sleep(1)
                    search_box = driver.find_element_by_id('autocomplete')
                    print(search_box.text)
                    search_box.click()

                    search_box.send_keys('chopper')
                    click_search_box = driver.find_element_by_class_name('flaticon-search')
                    search_box.send_keys(Keys.ENTER)
                    first_run = False

                except Exception as e:
                    traceback.print_exc()
                    print(f'{red}**ELEEMNT NOT FOUND CANNOT FIND SEARCH BOX {reset}\n {str(e)}]')
                    first_run = False
            else:
                pass

        print(OS)
        iterations_left = list_len - counter00
        print('X' * 50)
        print(f'**Total List Len [{list_len}]')
        print(f'**Completed Iteratiotions [{counter00}]')
        print(f'**Iterations Left [{iterations_left}]')
        print('X' * 50)
        time.sleep(7)
    except Exception as e:
        traceback.print_exc()
        print(f'{red}--[ERROR IN PARSING CHROME EXTENSION]{reset}\n {str(e)}')


    else:
        driver.implicitly_wait(25)
        search_box01 = driver.find_element_by_id('autocomplete')
        print(search_box01.text)
        search_box01.click()
        search_box01.send_keys(Keys.CONTROL, "a")
        search_box01.clear()
        print(f'starting list feed sequence\nThe List is [{list_len} long\n The Counter is at [{counter00}]')
        if counter00 >= 0 and counter00 <= list_len:
            #parser01 = TorrentParser()
            torrent_downloads = parser.list_iterator()
            print(f'Now Parsing.. {torrent_downloads}')
            search_box01.send_keys(torrent_downloads)
            # search_box01.send_keys(Keys.ENTER)

            time.sleep(.5)
            print('X' * 50)

            try:
                body = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'table-list-wrap'))
                    # EC.presence_of_all_elements_located((by.CLASS, 'table-list table table-responsive table-striped'))  ##
                )
                print(body.text)
                print(), print()
                href_link = body.find_element_by_xpath(
                    "/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
                print(href_link.text)

            except Exception as e:
                time.sleep(.5)
                print('X' * 50)
                print(f'{red}--[ERROR IN FINDING ELEMENTS XPATH]{reset}\n {str(e)}')
                traceback.print_exc()

        try:

            all_links = driver.find_element_by_xpath("//*[contains(@class, 'coll-1 name')]")
            if all_links:
                print('parsing all links\n', all_links.text)
                all_links.click()

            #  "//a[contains(@href,'" + _studnetID + "')]"

            #  "//a[contains(@href,'" + _studnetID + "')]"
            # driver.find_elements(By.XPATH("//*[contains(@class, 'coll-1 name')] or //a[contains(@href,'" + torrent_downloads + "')]")

            ## set up ax
            # single_link = driver.find_element_by_xpath("//a[contains(@href,'" + torrent_downloads + "')]")
            single_link = driver.find_element_by_xpath("//a[contains(@href, '/torrent/' )]")
            if single_link:
                print('single all links\n', single_link.text)
                single_link.click()

        except Exception as e:

                time.sleep(.5)
                print('X' * 50)
                print(f'{red}--[CANOT FIND ELEMENT IN DROPDOWN]{reset}\n {str(e)}')
                traceback.print_exc()
                print('X' * 50)

        ## open new tag

        try:
            torrent_dropdown = driver.find_element_by_class_name("dropdown")
            if torrent_dropdown:
                print('Torrent Dropdown\n', torrent_dropdown.text)
                counter00 += 1
                try:
                    download_href = driver.find_element_by_link_text('http://itorrents.org/')
                    # download_href = WebDriverWait(driver, 15).until( EC.presence_of_element_located((By.CLASS_NAME, "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))
                    if download_href:
                        print('**Commencing Download Chain')
                        action = ActionChains(driver)
                        action.click(on_element=download_href)  # click on key
                        action.send_keys(Keys.COMMAND + 't')  # send keys
                        action.perform()  # execute action
                        print('download_href \n', download_href.txt)
                        # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
                        download_href_click = driver.find_element_by_link_text('http://itorrents.org/').send_keys(Keys.COMMAND + 't')

                        counter00 += 1
                except Exception as e:
                    print('Exception in --[chained-action]-- cannot download link')
                    print(e)
                    pass

        except Exception as e:
            traceback.print_exc()
            print('Element not found click test', str(e))

        # x = '30'
        #
        # elif int(ticker) is range(x):
        #
        #     pass

    #
    # try:
    #     #  magnet = driver.find_element
    #     magnet_pull = WebDriverWait(driver, 15).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,
    #                                         "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))
    #
    #     )
    #     print('magnetpull info')
    #     print(magnet_pull.text)
    #
    #     print(magnet_link.text)
    #     magnet_link.click()
    #
    # except Exception as e:
    #     traceback.print_exc()
    #
    #     print('MAGNET PULL ERROR', str(e))
    #

# driver.quit()


# my_element00 = driver.find_element_by_class_name('') ## <--- pass in class value  #-> class styling method
# print(my_element00)

#
#  #### DROP DOWN CLASSES FOR MAGNET / TORRENT DOWNLOAD ##
# <ul class="lfa750b508ad7d04e3fc96bae2ea94a5d121e6607 lcafae12a818cf41a5873ad374b98e79512c946c6">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce" onclick="javascript: count(this);"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>Magnet Download</a> </li>
# <li class="dropdown">
# <a data-toggle="dropdown" class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c le41399670fcf7cac9ad72cbf1af20d76a1fa16ad" onclick="javascript: count(this);" href="#"><span class="icon"><i class="flaticon-le9f40194aef2ed76d8d0f7f1be7fe5aad6fce5e6"></i></span>Torrent Download</a>
# <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://itorrents.org/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2.torrent"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>ITORRENTS MIRROR</a> </li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://torrage.info/torrent.php?h=F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>TORRAGE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://btcache.me/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>BTCACHE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>None Working? Use Magnet</a></li>
#
