#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery
import re
import csv


browser = webdriver.PhantomJS()

def search_by_keyword(keyword, file_path, mode):
    print("正在搜索{}".format(keyword))
    try:
        url = "https://search.jd.com/Search?keyword=" + quote("手机") + "&enc=utf-8"
        browser.get(url)
        WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".gl-item"))
        )
        pages = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > em:nth-child(1) > b")
            )
        )
        datas = get_item_info()
        if len(datas) > 0:
            save_csv(file_path, mode, datas)
        print(pages.text)
        return int(pages.text)
    except TimeoutException as e:
        print("请求超时：", e)
        search_by_keyword(keyword)

def skip_page(page, file_path, mode):
    print("跳转到第{}页".format(page))
    try:
        input_text = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input"))
        )
        submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a"))
        )
        input_text.clear()
        input_text.send_keys(page)
        submit.click()
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"))
        )
        datas = get_item_info()
        if len(datas) >0:
            save_csv(file_path, mode, datas)
    except TimeoutException as e:
        print("请求超时：", e)
        skip_page(page, file_path, mode)

def get_item_info():
    html = browser.page_source
    print(html)
    pq = PyQuery(html)
    items = pq(".gl-item").items()
    datas = []
    head = ["p-name", "href", "p-price", "p-commit", "p-shop","p-icons"]
    datas.append(head)
    for item in items:
        p_name = re.sub('\\n', '', item.find('.p-name em').text())
        href = item.find('.p-name a').attr('href')
        p_price = item.find('.p-price').text()
        p_commit = item.find('.p-commit').text()
        p_shop = item.find('.p-shop').text()
        p_icons = item.find('.p-icons').text()
        info = []
        info.append(p_name)
        info.append(href)
        info.append(p_price)
        info.append(p_commit)
        info.append(p_shop)
        info.append(p_icons)
        print(info)
        datas.append(info)
    return datas

def save_csv(file_path, mode, datas):
    with open(file_path, mode) as f:
        writer = csv.writer(f)
        writer.writerows(datas)

def main():
    try:
        keyword = "手机" #搜索关键词
        file_path = "./jd_mobile_phone_page1"
        write_mode = "w"
        pages = search_by_keyword(keyword,file_path,write_mode)
        print("搜索结果共{}页".format(pages))
        #按照顺序循环跳转到下一页
        for page in range(2, pages + 1):
            file_path = "./jd_mobile_phone_page" + str(page)
            skip_page(page,file_path,write_mode)
    except Exception as err:
        print("产生异常：",err)
    finally:
        browser.close()


if __name__ == '__main__':
    main()




