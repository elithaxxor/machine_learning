import requests, json, io, os, sys, traceback
from configparser import ConfigParser
from requests import get
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from fake_useragent import UserAgent  ## module to better spoof headers
from config import *
from requests import Request, Session
import base64 as b64


# Standard library imports...
# from unittest.mock import Mock, patch
# from nose.tools import assert_is_not_none
''' 
## https://realpython.com/testing-third-party-apis-with-mocks/
## WILL NOT WORK IF SERVER RESPONSE != 200 
## 1. start server/make request to test server.
## 2. Send Request to test server. 
## 3. kill program in entirety if assert_is_not_none for response 
'''
#
# @patch('bsreg.services.requests.get')
# def test_getting_todos(mock_get):
#     mock_get = mock_get_patcher.start()
#     mock_get.return_value.ok = True
#     response = get_todos(); print(response)
#     print(f'MOCK_VALUES, {mock_get.return_value}\n\n [RESPONSE] {response}')
#     mock_get_patcher.stop()
#     assert_is_not_none(response)
# try:
#     from urllib.parse import urljoin
# except ImportError:
#     from urlparse import urljoin


'''
is to ignore the fact that the session token is unknown, and simply proceed to generate a new session token and create a new session 
for it. The initial state of the session will of course be "not-yet-authenticated", so if the user is trying to access a non-public page, then 
the page will see to it that they receive an HTTP 401 "Unauthorized (Unauthenticated)" and must authenticate. But if the user lands on a public page, 
they won't notice anything different.
SOLUTION:
try: 
with a login/password form, avoiding to tranfer the user to another page.
'''
''' 
 need to use a session object and send the authentication each request. The session will also track cookies for you:
session = requests.Session()
session.auth = (user, password)
auth = session.post('http://' + hostname)
response = session.get('http://' + hostname + '/rest/applications')
'''




class Authenticator():
    def __init__(self):
        super().__init__()
        self.header = requests.utils.default_headers()
        self.count = 0
        self.URL = r"https://google.com/"
        self.path = os.getcwd()

    ## object readibility
    @property
    def __str__(self):
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args))  ## guidelines for repr
    @property
    def __repr__(self):
        #return '{}({})'.format(type(self).__name__, ', '.join(str(getattr(self, a)) for a in self._args))
        return f'header is \n\n {self.header} and the count is: {self.count}'

    def __enter__(self):
        print(f'[-] [EXC_TYPE] \n{exc_value} \n\n[-] [exc_value]\n\n[-] [TRACEBACK-ERROR] \n[{traceback.format_exc}]')
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'[-] [EXC_TYPE] \n{exc_value} \n\n[-] [exc_value]\n\n[-] [TRACEBACK-ERROR] \n[{traceback.format_exc}]')

    @staticmethod
    def write_parsed_info(*args):
        with open('request_hist.txt', 'a') as f:
            f.writelines(*args)

            #f.writeline('r_loc_history', r_loc_history)
           # f.write(history)

    @staticmethod
    def read_config_ii():
        #config_loc = os.getcwd() + "/config.json"
        with open("config_str.json", 'r') as f:
            config_data = json.loads(f.read())
        USER, PASS = config_data.get('USER'), config_data.get('PASS')
        return USER, PASS


    def initiate(self):
        self.count += 1
        '''handle_cookie_error'''
        def reauth(history, r):

            ## Extrapolate cookie information
            for cookie in response.cookies:
                print('cookie domain = ' + cookie.domain); print('cookie name = ' + cookie.name)
                print('cookie value = ' + cookie.value); print('X' * 50), print()
            for item in cookies.iterkeys():
                print(item)


            old_url = str(r.url)
            r = requests.head(url, allow_redirects=True)
            print(r.url)
            if old_url != str(r.url): ## if new URL, return value; else continue working.
                return True

            auth_timeout = random.randint(0, 1.5)
            time.sleep(auth_timeout)
            print("Status Code returned an error.  Attempting solve the issue. \n ", r.status_code)

            time.sleep(auth_timeout)
            print("Status Code: 401 or 404. Below is the connection history \n ", history)
            # r = requests.get(self.url, cookies=cookies) --> called it in the main function's exception.

            for i, resp in enumerate(r.history, 1):
                print("X" * 50, "\n [+] " + str(i) + " - URL " + resp.url + " \n")
                print('\t', resp.status_code, resp.url)

            print('[-]Potential Redirect Present: ')  ## add code to further scarpe site and find module.

            del r.headers['cookies-name']
            r.headers.update({'': 'true',})  # edit header object, make x-test true
            s.headers.update({'x-test': 'true',})  # edit header object, make x-test true
            s.headers.update({'cookies-name':'r.cookie',})

            print('s.headers', s.headers); print('r.headers', r.headers)
            print('NEW COOKIE: ', r.cookie); print('NEW STATUS-CODE: ', r.status_code, r.url)
           # if not r.ok:
            if r.status_code != 200:  ## Check if return URL is provided
                old_url = str(r.url)
                r = requests.head(url, allow_redirects=True)
                print(r.url)
                if old_url != str(r.url):  ## if new URL, return value; else continue working.
                    return True
            if not s.ok or r.status_code == 200:
                return True
            print(f'[REQUEST HISTORY]:\n {r.history}\n\n\n[SEND HISTORY]:\n{s.history}')

        '''handle_301_ERROR'''
        def reauth301(history):
            '''
                * This function will handle '301' redirects by searching redirect logs and handling a few commmon errors.
                * I plan to add a crawler to find a module down the line.')
                https://stackoverflow.com/questions/20475552/python-requests-library-redirect-new-url
            '''
            try:
                i=0
                auth_timeout = random.randint(0, 1.5); time.sleep(auth_timeout)
                print('[OLD_LOCATION]', r.history[0].headers['Location'])
                print("Status Code: 301. Below are the redirects\n ", history)
                del r.headers['Location']
                ## print list of repsonse codes
                for resp in r.history:
                    print("X"*50, "\n [+] " + str(i) + " - URL " + resp.url + " \n")
                    print('\t', resp.status_code, resp.url)
                    i+=1
                print('[-]Potential Redirect Present: ', i)  ## add code to further scarpe site and find module.
            except requests.exceptions.ConnectionError:
                print("Connection Error.", traceback.print_exc())
            except requests.exceptions.Timeout:
                print("Timeout Error.", traceback.print_exc())
            except requests.exceptions.TooManyRedirects:
                print("There were too many redirects.", traceback.print_exc())

        def var_to_b64(string_var):
            arr = bytes(string_var, 'utf-8')
            print(arr, '\n')
            for byte in arr:
                print(byte, end=' ')
            print("\n")


        '''## END OF NESTED FUNCTIONS, STARTING METHOD ##'''

        while True:
            try:
                global s, r

                ## header.update is used for initial requests probe.
                self.header.update(
                    {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                    }
                )

                ## retrieve header from site, update cookiesm, check if reauth is needed. redirect appropiatly if new handshake needed.
                r = requests.get(self.URL)
                req_status = r.status_code
                r_cookies = r.cookies
                r_headers = r.request.headers

                ## creates a log of LOCATION history.
                if r.history:
                    r_loc_history=[]
                    print(f" [HISTORY] {r.history}, \n [REQUEST-HEADERS]\n {r.request.headers} \n [COOKIES] \n {r.cookies}")
                    history = r.history[0].headers['Location']
                    r_loc_history.append(history)
                    Authenticator.write_parsed_info(r_loc_history)


                ''' 
                    * ##### TRY / EXCEPTION MAY CATCH THIS ####
                    * Take 301 re-route and update location
                    * else, update cookie, and set new coookies 
                 '''

                print(r.status_code)
                if r.status_code == 301: # check for 301 redirect, update request with new loc
                    new_location = r.history[0].headers['Location']
                    doConnect = reauth301(new_location)
                    if bool(r.history[0].headers['Location']) is True:
                        print(r.status_code)
                ## update the headers from requests
                elif not r.ok:
                    self.header.update({'cookieKey': r.cookies})
                ## set new session using prepped headers, and updating possible new location from request headers.
                elif not r.ok:
                    r = s.get(f'{self.URL} / cookies')
                    print(r, s.cookies.get_dict())
                    s = requests.Session()
                    req = Request('GET', self.URL, data=data, headers=self.headers)
                    prepped = s.prepare_request(req)
                    new_location = r.history[0].headers['Location']
                    prepped.headers['Location'] = new_location
                    resp = s.send(prepped,
                                  stream=stream,
                                  verify=verify,
                                  proxies=proxies,
                                  cert=cert,
                                  timeout=timeout
                                  )
                    print(resp.status_code)
                    print(resp.text)
                print('request status code' ,r.status_code)

                #### End of test set user/pass var with config file
                USER, PASS = Authenticator.read_config_ii()
                try:
                    if bool(s) is False:
                        print('session not initiated is false')
                        pass
                except Exception as e:print(str(e))


                s = requests.Session()
                s.auth = (USER, PASS)
                s_cookies = s.cookies.get_dict()
                print('X' * 50)
                print('x'*50, s ,'\n' ,dir(s)); print('x'*50)
                print('[COOKIE-CHECK]" ', bool(s_cookies), '\n', '[AUTH-CHECK]" ', bool(s.auth),'\n' ,'[AUTH-CHECK]" ', (s.auth))
                if bool(s_cookies) is False:
                    self.header.update({'cookieKey':'s_cookies'})
                    print(self.header)

                ### MAY NOT BE NECSSARY SINCE HEADERS ARE UPDAETD s.cookies.set
                self.header.update({'cookieKey':'s_cookies'})
                print('updated header: \n',self.header)
                s.headers.update({'x-test': 'true'}) # edit header object, make x-test true
                response = s.get(self.URL)
                print(response); print('X'*50)


                ## to check for unsignd SSL/SSH project
                try:
                    requests.get(f'{self.URL}+.in')
                    print(s.cookies.get_dict()) ## to get dict of cookies
                except Exception as e: print('[UNSIGNED OR NON-EXIST SSL PATH]\n\n', str(e), '\n', traceback.print_exc())
                print('X'*50)
                print(f'[BASE-URL]\n, {self.URL} \n')
                print(f'{s.auth}, \n {type(s.auth)}')
                print(f'[CLIENT-COOKIES] \n [SERVER-HEADER] {r_cookies}')
                print(f'[RESPONSE], {response}\n [SERVER-HEADER] {s.headers}')
                print(f'[RESPONSE], {response}\n {s_cookies}')
                print(f'[AUTH-Encoded-Debug]', var_to_b64(USER), var_to_b64(PASS)) #encrypt AES or delete.
                print(s.cookies.get_dict(), '\nX'*50)
                self.count +=1
                print('X'*50)

                ### INSERT END OF LIST HERE ###
                ### IF LEN OF REQUEST LIST REACHED, BREAK AND CLOSE CONNECTION.
                #break

            ## The exception is intended to catch 404, 401, and 301 errors, and request new cookies to be passed into nested function
            except HTTPError as e:
                if e.response.status_code == 404:
                    time.sleep(auth_timeout)
                    r = s.get(f'{self.URL} / cookies'); print(r.text, r.cookies, s.cookies.get_dict())
                    print('ERROR 404: (page not found)\n ', e,'\n', traceback.print_exc()); reauth(r)
                elif e.response.status_code == 401:
                    time.sleep(auth_timeout)
                    r = s.get(f'{self.URL} / cookies')
                    print(r.text, r.cookies, s.cookies.get_dict())
                    print('ERROR 401: (Lackin\'n requird docs) ', e, '\n', traceback.print_exc()); reauth(r) #return False

                elif e.response.status_code == 301:
                    time.sleep(auth_timeout)
                    r = s.get(f'{self.URL} / cookies')
                    print(r.text, r.cookies, s.cookies.get_dict()); reauth301(r)
                    print('ERROR 301: (Moved Perminantly)', e,'\n', traceback.print_exc())



## user repr to use __repr__ context manager and return object values.
def main():
    header = requests.utils.default_headers()  ## default, unassigned headers
    startAuthenticator = Authenticator()
    startAuthenticator.initiate()

    print(repr(startAuthenticator))
    count = 0
    #path = os.getcwd()
    print('Function REsopnse REcevied' , resp)
    if resp is False:
        print(f'{repr(startAuthenticator)} \n HTTP Return other than 200, proceeding to reauthenticate. ')
        time.sleep(auth_timeout)
        count += 1
    elif resp == fail_req:
        print(f'{repr(startAuthenticator)} \n failed [RESPONSE]', resp); reauth()
    elif resp == fail_sesh:
        print(f'{repr(startAuthenticator)} \n failed [SESSION]', resp); reauth()
    elif resp == 301: # redirect to 301 function instead of 400s
        print(f'{repr(startAuthenticator)} \n301 response, attempting to redirect ', resp); reauth301()
        #
    print(resp)

#<form class="fh-form" data-el-action="" data-el="FormSignin" data-el-ajax data-el-auth data-el-global-error-container="#global-error-creatorView" novalidate data-el-prefix="fh">…</form>

### START SEQUENCE ###
if __name__ == '__main__':
    main()
    ## close session ##
    print(f'End of session, system reauthed  times. \n proceeding confirm client-session exit, then shutdown.')
    with requests.Session() as s:
        while True:
            time.sleep(3)
            s.get('URL') ## use cookies to check if the session closed between server and client.
            if s.get == 200:
                continue
            sys.exit(1)
#



