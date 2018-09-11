# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class zhihu_question_item(scrapy.Item):
    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    question_url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()


    def get_insert_sql(self):
        insert_sql = """
        insert into zhihu_question (topics, zhihu_id, url, title, content, answer_num, 
        comments_num, watch_user_num, click_num, crawl_time) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         ON DUPLICATE KEY UPDATE content=VALUES (content), 
        answer_num = VALUES (answer_num),comments_num = VALUES (comments_num)"""


        params = (self['topics'], self['zhihu_id'], self['question_url'], self['title']
                  , self['content'], self['answer_num'], self['comments_num'], self['watch_user_num'],
                  self['click_num'], self['crawl_time'])


        return insert_sql, params

class zhihu_anwser_item(scrapy.Item):
    answer_id = scrapy.Field()
    question_title = scrapy.Field()
    question_created_time = scrapy.Field()
    question_updated_time = scrapy.Field()
    author_name = scrapy.Field()
    answer_content = scrapy.Field()
    answer_image_urls = scrapy.Field()
    answer_praise_num = scrapy.Field()
    answer_comment_num = scrapy.Field()




    def get_insert_sql(self):

        insert_sql = """
        insert into zhihu_answer (question_title, answer_id, author_name, answer_content, answer_praise_num, answer_comment_num) 
         VALUES (%s, %s, %s, %s, %s, %s)
         ON DUPLICATE KEY UPDATE answer_content=VALUES (answer_content), 
        answer_praise_num = VALUES (answer_praise_num),answer_comment_num = VALUES (answer_comment_num)"""

        params = (self['question_title'], self['answer_id'], self['author_name'], self['answer_content']
                  , self['answer_praise_num'], self['answer_comment_num'])

        return insert_sql, params



    # answer_item['answer_id'] = answer_id
    # answer_item['question_title'] = question_title
    # answer_item['question_created_time'] = question_created_time
    # answer_item['question_updated_time'] = question_updated_time
    # answer_item['author_name'] = author_name
    # answer_item['answer_content'] = answer_content
    # answer_item['answer_image_urls'] = answer_image_urls
    # answer_item['answer_praise_num'] = answer_praise_num
    # answer_item['answer_comment_num'] = answer_comment_num




