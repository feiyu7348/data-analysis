# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/29

import re
import csv
import hashlib


def get_words():
    # 读取数据
    with open('word2count.txt') as fp:
        text = fp.read()

    text = text.lower()  # 所有字母改为小写
    words = re.findall("\w*", text)  # 正则匹配
    words = [x for x in words if x != '']  # 删除空字符
    words = list(filter(lambda x: not str(x).isdigit(), words))  # 删除数字
    return words


# md5转化
def md5_convert(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


def count_words(words):
    b = []  # 存放数据
    while len(words) > 0:
        word = words.pop(0)  # 删除第一个单词赋给新列表word
        count = words.count(word) + 1  # 计算总数
        for _ in range(count - 1):  # 删除单词列表中的相同元素
            words.remove(word)
        b.append([word, count])  # 存起来,count为该单词出现次数

    # 先对单词的md5值排序
    for i in range(len(b)):
        md5_convert(b[i][0])
    b.sort(reverse=True)
    # 获取b中数字的个数 后面对次数从大到小进行排序
    array = []
    for i in range(len(b)):
        array.append(b[i][1])
    array.sort(reverse=True)
    return array, b


# 打印
def print_words(array, b):
    results = []
    for n in list(reversed(list(set(array)))):  # 集合去重打印
        for i in range(len(b)):
            if b[i][1] == n:
                # print("{}出现{}次".format(b[i][0], n))
                results.append([b[i][0], n])
    return results


# 写入csv文件
def write_csv(results):
    with open("张飞宇_20210629_word_result.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)


if __name__ == '__main__':
    array, b = count_words(get_words())
    result = print_words(array, b)
    write_csv(result)


