# -*- coding: utf-8 -*-
import json

import scrapy
import re
from urllib import parse
from scrapy.http import Request
import datetime

from zhihu_spider.function.common import str_to_int
from zhihu_spider.items import zhihu_question_item, zhihu_anwser_item


class ZhihuSpider(scrapy.Spider):
    name = 'images_spider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    start_answer_urls = ['https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest%27_answerer%29%5D.topics&limit={1}&offset={2}&sort_by=default']


    def start_requests(self):
        #使用selenium模拟登录知乎
        from selenium import webdriver
        browser = webdriver.Firefox(executable_path='/home/maruimin/Downloads/geckodriver')
        browser.get('https://www.zhihu.com/signin')

       # browser.find_element_by_css_selector('.SignContainer-switch span').click()
        browser.find_element_by_css_selector('.SignFlow-account input[name="username"]').send_keys('13883270441')
        browser.find_element_by_css_selector('.SignFlow-password input[name="password"]').send_keys('555dedd+5')
        browser.find_element_by_css_selector('button.SignFlow-submitButton').click()

        import time
        time.sleep(10)

        Cookies = browser.get_cookies()
        cookie_dict = {}
        import pickle
        for cookie in Cookies:
            f = open('/home/maruimin/zhihu_cookies/'+cookie['name']+'.zhihu', 'wb')
            pickle.dump(cookie, f)
            f.close()
            cookie_dict[cookie['name']] =cookie['value']
        browser.close()
        for url in self.start_urls:

            return [scrapy.Request(url=url, dont_filter=True, cookies=cookie_dict)]




    def parse(self, response):
        key_word = input('请输入要搜索的内容')
        search_url = 'https://www.zhihu.com/search?type=content&q={}'.format(key_word)
        yield scrapy.Request(search_url, callback=self.search_reslut)


    def search_reslut(self, response):

        #解析提问里面的相关数据，并在最后跳转到parse_answer里面取解析回答里面的数据

        all_urls = response.css('a::attr(href)').extract()
        for url in all_urls:
            match_obj = re.match('(.*question/(\d+))(/|$)', parse.urljoin(response.url, url))
            if match_obj:
                question_url = match_obj.group(1)
                question_id = match_obj.group(2)
                yield Request(url=question_url, meta={'zhihu_id': question_id}, callback=self.parse_question)




    def parse_question(self, response):

        zhihu_id = response.meta.get('zhihu_id')
        yield scrapy.Request(self.start_answer_urls[0].format(zhihu_id, 20, 0), callback=self.parse_answer)



    def parse_answer(self, response):
        answer_dict = json.loads(response.text)

        for answer in answer_dict['data']:
            answer_id = answer['id']

            question_title = answer['question']['title']

            question_created_time = answer['question']['created']

            question_updated_time = answer['question']['updated_time']

            author_name = answer['author']['name']

            answer_content = answer['content']

            answer_image_urls = re.findall('data-actualsrc="(.*?)\"', answer_content, re.DOTALL)   #获取文章中所有图片url的链接

            answer_praise_num = answer['voteup_count']

            answer_comment_num = answer['comment_count']



            #将parse_answer里面爬取到的信息录入到item中来
            answer_item = zhihu_anwser_item()
            answer_item['answer_id'] = answer_id
            answer_item['question_title'] = question_title
            answer_item['question_created_time'] = question_created_time
            answer_item['question_updated_time'] = question_updated_time
            answer_item['author_name'] = author_name
            answer_item['answer_content'] = answer_content
            answer_item['answer_image_urls'] = answer_image_urls
            answer_item['answer_praise_num'] = answer_praise_num
            answer_item['answer_comment_num'] = answer_comment_num

            yield answer_item


        if answer_dict['paging']['is_end'] == False:    #判断还有没有下一页的数据
            next_page_url = answer_dict['paging']['next']
            yield scrapy.Request(next_page_url, callback=self.parse_answer)
