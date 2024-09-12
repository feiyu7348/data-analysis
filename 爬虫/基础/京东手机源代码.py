'''
爬取京东手机商品信息
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery
from urllib.parse import quote
import csv
import re

# 构建一个无界面的浏览器对象
browser = webdriver.PhantomJS()

'''
功能：根据关键词搜索，解析网页数据,将数据保存到CSV文件中
参数：
    keyword：搜索关键词
    file_path：CSV文件路径
    mode：写入模式
返回值：搜索结果总页数
'''


def search_by_keyword(keyword, file_path, mode):
    print("正在搜索{}".format(keyword))
    try:
        url = "https://search.jd.com/Search?keyword=" + quote("手机") + "&enc=utf-8"
        browser.get(url)
        # 等待网页内容加载完成
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".gl-item"))
        )
        # 浏览器发送请求后最多等待10秒钟，直到页码导航中的共...页加载完成，然后取出总页数
        pages = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > em:nth-child(1) > b"))
        )
        # 解析网页源代码,获取想要的商品信息
        datas = get_item_info()
        if len(datas) > 0:
            # 将数据保存到CSV文件中
            save_csv(file_path, mode, datas)
        print(pages.text)
        return int(pages.text)
    # 捕捉超时异常
    except TimeoutException as e:
        print("请求超时：", e)
        search_by_keyword(keyword)  # 请求超时，重试


'''
功能：跳转到指定页码的网页，解析网页数据，将数据保存到CSV文件中
参数：
    page：页码
    file_path：CSV文件路径
    mode：写入模式
'''


def skip_page(page, file_path, mode):
    print("跳转到第{}页".format(page))
    try:
        # 获取跳转到第几页的输入框
        input_text = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input"))
        )
        # 获取跳转到第几页的确定按钮
        submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a"))
        )
        print(type(input_text))
        print(type(submit))
        input_text.clear()  # 清空输入框
        input_text.send_keys(page)  # 在输入框中填入要跳转的页码
        submit.click()  # 点击确定按钮

        # 等待网页加载完成，直到页面下方被选中并且高亮显示的页码，与页码输入框中的页码相等
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page))
        )

        datas = get_item_info()
        if len(datas) > 0:
            save_csv(file_path, mode, datas)

    except TimeoutException as e:
        print("请求超时：", e)
        skip_page(page, file_path, mode)  # 请求超时，重试


'''
功能：解析网页数据
返回值：商品信息列表
'''


def get_item_info():
    # 获取网页源代码
    html = browser.page_source
    print(html)
    # 使用PyQuery解析网页源代码
    pq = PyQuery(html)
    # 获取源代码中所有的class="gl-item"的<li>列表项,每一对<li class="gl-item">...</li>是一个商品信息
    items = pq(".gl-item").items()
    datas = []
    # 表头
    head = ["p-name", "href", "p-price", "p-commit", "p-shop", "p-icons"]
    datas.append(head)
    for item in items:
        p_name = re.sub("\\n", "", item.find(".p-name em").text())  # 商品名称，使用正则表达式将商品名称中的换行符\n替换掉
        href = item.find(".p-name a").attr("href")  # 商品链接
        p_price = item.find(".p-price").text()  # 商品价钱
        p_commit = item.find(".p-commit").text()  # 商品评价
        p_shop = item.find(".p-shop").text()  # 店铺名称
        p_icons = item.find(".p-icons").text()
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


'''
功能：将商品信息写入CSV文件
参数：
    file_path：CSV文件路径
    mode：写入模式
    datas：商品信息列表
'''


def save_csv(file_path, mode, datas):
    with open(file_path, mode) as f:
        writer = csv.writer(f)
        writer.writerows(datas)


def main():
    try:
        keyword = "手机"  # 搜索关键词
        file_path = "./jd_mobile_phone_page1"
        write_mode = "w"
        pages = search_by_keyword(keyword, file_path, write_mode)
        print("搜索结果共{}页".format(pages))
        # 按照顺序循环跳转到下一页
        for page in range(2, pages + 1):
            file_path = "./jd_mobile_phone_page" + str(page)
            skip_page(page, file_path, write_mode)
    except Exception as err:
        print("产生异常：", err)
    finally:
        browser.close()


if __name__ == '__main__':
    main()
