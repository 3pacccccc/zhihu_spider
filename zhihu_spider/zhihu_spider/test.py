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



    # browser = webdriver.Firefox(executable_path='/home/maruimin/Downloads/geckodriver')
    #
    # browser.get('http://93.91p18.space/index.php')
    #
    #
    # browser.find_element_by_css_selector('.SignContainer-switch span').click()
    # browser.find_element_by_css_selector('.SignFlow-account input[name="username"]').send_keys('13883270441')
    # browser.find_element_by_css_selector('.SignFlow-password input[name="password"]').send_keys('555dedd+5')
    # browser.find_element_by_css_selector('button.SignFlow-submitButton').click()
    # #browser.quit()
    # print(browser.page_source)

# browser = webdriver.Firefox(executable_path='/home/maruimin/Downloads/geckodriver')
# browser.get('https://qzone.qq.com/')
# browser.find_element_by_css_selector('#bottom_qlogin a#switcher_plogin').click()




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

#gitee_login('mage2333', '351489917mrm')
#get_authenticity_token()

#login_by_cookie()


content = """<p>程序员圈子内女生确实很少，颜值高的就更少了，高颜值加气质好的已经是寥寥无几了，而颜值高又有才又有气质的的我至今只认识一个 <a class=\"member_mention\" href=\"https://www.zhihu.com/people/39e1a1e41b3903f9283e13d11a39bbfd\" data-hash=\"39e1a1e41b3903f9283e13d11a39bbfd\" data-hovercard=\"p$b$39e1a1e41b3903f9283e13d11a39bbfd\">@玲珑邪僧</a></p><p>说实话：</p><p>照片还不如本人漂亮；</p><p>真人的气质是由内而外透露出来的；</p><p>不高冷又幽默，</p><p>认真又很调皮，</p><p>很难想象一些见解很深刻的区块链技术文章出自她手，而认识了之后才知道为了写一篇文章她会耗时多久、翻阅多少的书籍，佩服得五体投地。</p><p>这样的女性不要说是在程序员圈，在哪个圈都算是非常非常优秀的了。</p><p><br></p><p>她是我至今认识的最优秀的女性程序员，第二优秀的女性。</p><p>这么多照片呢，不点赞吗？！</p><figure><noscript><img src=\"https://pic2.zhimg.com/v2-2589423dc6be6926d13b0e71d4786fed_b.jpg\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"1000\" data-rawheight=\"1333\" class=\"origin_image zh-lightbox-thumb\" width=\"1000\" data-original=\"https://pic2.zhimg.com/v2-2589423dc6be6926d13b0e71d4786fed_r.jpg\"></noscript><img src=\"data:image/svg+xml;utf8,&lt;svg%20xmlns='http://www.w3.org/2000/svg'%20width='1000'%20height='1333'&gt;&lt;/svg&gt;\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"1000\" data-rawheight=\"1333\" class=\"origin_image zh-lightbox-thumb lazy\" width=\"1000\" data-original=\"https://pic2.zhimg.com/v2-2589423dc6be6926d13b0e71d4786fed_r.jpg\" data-actualsrc=\"https://pic2.zhimg.com/v2-2589423dc6be6926d13b0e71d4786fed_b.jpg\"></figure><figure><noscript><img src=\"https://pic2.zhimg.com/v2-91e813a3df3d49bc9eb306f1dc0ea045_b.jpg\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"960\" data-rawheight=\"1280\" class=\"origin_image zh-lightbox-thumb\" width=\"960\" data-original=\"https://pic2.zhimg.com/v2-91e813a3df3d49bc9eb306f1dc0ea045_r.jpg\"></noscript><img src=\"data:image/svg+xml;utf8,&lt;svg%20xmlns='http://www.w3.org/2000/svg'%20width='960'%20height='1280'&gt;&lt;/svg&gt;\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"960\" data-rawheight=\"1280\" class=\"origin_image zh-lightbox-thumb lazy\" width=\"960\" data-original=\"https://pic2.zhimg.com/v2-91e813a3df3d49bc9eb306f1dc0ea045_r.jpg\" data-actualsrc=\"https://pic2.zhimg.com/v2-91e813a3df3d49bc9eb306f1dc0ea045_b.jpg\"></figure><figure><noscript><img src=\"https://pic3.zhimg.com/v2-79fce7cc736a64dfb652ab6164c038e2_b.jpg\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"772\" data-rawheight=\"800\" class=\"origin_image zh-lightbox-thumb\" width=\"772\" data-original=\"https://pic3.zhimg.com/v2-79fce7cc736a64dfb652ab6164c038e2_r.jpg\"></noscript><img src=\"data:image/svg+xml;utf8,&lt;svg%20xmlns='http://www.w3.org/2000/svg'%20width='772'%20height='800'&gt;&lt;/svg&gt;\" data-caption=\"\" data-size=\"normal\" data-rawwidth=\"772\" data-rawheight=\"800\" class=\"origin_image zh-lightbox-thumb lazy\" width=\"772\" data-original=\"https://pic3.zhimg.com/v2-79fce7cc736a64dfb652ab6164c038e2_r.jpg\" data-actualsrc=\"https://pic3.zhimg.com/v2-79fce7cc736a64dfb652ab6164c038e2_b.jpg\"></figure>"""
#match_obj = re.findall('.*data-original="(.*)".*', content, re.DOTALL)
#match_obj = re.findall('(\d+)', content)
match_obj = re.findall('data-actualsrc="(.*?)\"', content, re.DOTALL)
if match_obj:
    print(match_obj.group(1))




