# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import MySQLdb
import pymongo
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class QidianHotPipeline:
    def __init__(self):
        self.author_set = set()

    def process_item(self, item, spider):
        if item["name"] in self.author_set:
            raise DropItem("查找到重复姓名的项目：%s" % item)
        return item

class MySQlPipeline(object):
    def open_spider(self, spider):  # 在spider开始之前，调用一次
        db_name = spider.settings.get('MYSQL_DB_NAME', 'qidian')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        user = spider.settings.get('MYSQL_USER', 'root')
        pwd = spider.settings.get('MYSQL_PASSWORD', '123456')
        # 链接数据库
        self.db_conn = MySQLdb.connect(
            db=db_name,
            host=host,
            user=user,
            password=pwd,
            charset="utf8"
        )
        self.db_cursor = self.db_conn.cursor()  # 得到游标

    def process_item(self, item, spider):  # 处理每一个item
        values = (item["name"], item["author"], item["type"], item["form"])
        # 确定sql
        sql = "insert into hot(name,author,type,form) values(%s, %s, %s, %s)"
        self.db_cursor.execute(sql, values)
        return item

    def close_spider(self, spider):  # 在spider结束时，调用一次
        self.db_conn.commit()  # 提交数据
        self.db_cursor.close()
        self.db_conn.close()


class MongoDBPipeline(object):
    def open_spider(self, spider):  # 在spider开始之前，调用一次
        host = spider.settings.get("MONGODB_HOST", "localhost")
        port = spider.settings.get("MONGODB_PORT", 27017)
        db_name = spider.settings.get("MONGODB_NAME", "qidian")
        collection_name = spider.settings.get("MONGODB_COLLECTION", "hot")
        self.db_client = pymongo.MongoClient(host=host, port=port)  # 客户端对象
        # 指定数据库
        self.db = self.db_client[db_name]
        # 指定集合
        self.db_collection = self.db[collection_name]

    def process_item(self, item, spider):  # 处理每一个item
        item_dict = dict(item)
        self.db_collection.insert_one(item_dict)

    def close_spider(self, spider):  # 在spider结束时，调用一次
        self.db_client.close()







