# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class ZhihuSpiderPipeline(object):
    def process_item(self, item, spider):
        return item




class zhihu_image_spider_pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
            for image_url in item['answer_image_urls']:
                yield Request(url=image_url, meta={'item': item})


    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('item contains no image')

        return item


    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        file_names = 'zhihu_images/%s/%s/%s' % (item['question_title'], item['author_name'], image_guid)
        return file_names







class mysqltwistedpipeline(object):


    def __init__(self,dbpool):
        self.dbpool = dbpool



    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )



        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)

        return cls(dbpool)


    def process_item(self, item, spider):
        querry = self.dbpool.runInteraction(self.do_insert, item)
        querry.addErrback(self.handle_error)


    def handle_error(self,failure):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()

        cursor.execute(insert_sql, params)





