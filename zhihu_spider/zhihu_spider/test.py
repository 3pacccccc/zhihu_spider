# -*- coding:utf-8 -*-
import datetime
import re

__author__ = 'maruimin'

from selenium import webdriver
import requests
from scrapy.selector import Selector
try:
    import cookielib
except:
    import http.cookiejar as cookielib




session = requests.session()
session.cookies = cookielib.MozillaCookieJar(filename='cookie.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('fail to load cookies')
    
    
    
def get_authenticity_token():
    response = session.get('https://gitee.com/login')
    # content="RBQxUFQGDLD/7o/t1+QDk1at3xxHgu4M0ebKxw5yBjg=" name="csrf-token"
    authenticity_token_re = re.match('.*content="(.*?)" name="csrf-token"',response.text, re.DOTALL)
    # text = Selector(text=response.text)
    # authenticity_token = text.css('meta[name="csrf-token"]::attr(content)').extract_first('')
    if authenticity_token_re:
        print(authenticity_token_re.group(1))


def login_by_cookie():
    res = session.get('https://gitee.com/login')
    return res

def gitee_login(account, password):
    post_data = {
        'utf8': "✓",
        'authenticity_token': get_authenticity_token(),
        'redirect_to_url': '/mage2333/events',
        "user[login]": account,
        "user[password]": password,
        'captcha': '',
        'user[remember_me]': '1',
        'commit': 'sign+in'
    }
    response_after_login = session.post('https://gitee.com/login', data=post_data)

    session.cookies.save()










