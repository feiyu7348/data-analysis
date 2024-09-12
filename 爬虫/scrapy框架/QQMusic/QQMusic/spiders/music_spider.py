import scrapy
import json
from scrapy import Request
from QQMusic.items import QqmusicItem


class MusicSpider(scrapy.Spider):
    name = 'music'

    def start_requests(self):
        url = "https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI26245077641608616&g_tk=5381&sign=zza9wpks9kyagdd305df002e89318f8d3f7f700cb95c1d2&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222021-07-05%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
        yield Request(url)

    def parse(self, response):
        json_text = response.text
        music_dict = json.loads(json_text)
        for one_music in music_dict["detail"]["data"]["data"]["song"]:
            item = QqmusicItem()
            item["song_name"] = one_music["title"]
            item["singer_name"] = one_music["singerName"]
            yield item
