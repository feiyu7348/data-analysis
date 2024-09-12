# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/29


"""
1.请编写Python脚本，统计附件“word2count.txt”中的英文单词（仅英文单词，忽略大小写）的出现频次，并将统计结果保存在与
“word2count.txt”同级目录下，名字为 “本人姓名”+“_”+“8位日期”+“_”+“word”+“_”+“result.csv”的表格文件中
（如：姚明_20200302_word_result.csv），结果文件中按出现频次由高往低的顺序依次排列，A列为单词，B列为出现频次（频次相同以单词的MD5值排序）。
"""

import re
import csv


def get_words():
    with open('word2count.txt') as fp:
        text = fp.read()

    words = re.findall("\w*", text)
    for word in words:  # 删除空字符串
        if word == '':
            words.remove('')
    words = list(filter(lambda x: not str(x).isdigit(), words))  # 删除数字
    return words


def count_words(words):
    b = []  # 存放数据
    while len(words) > 0:
        word = words.pop(0)  # 删除第一个单词赋给新列表a
        count = words.count(word) + 1  # 计算总数
        for _ in range(count - 1):  # 删除单词列表中的相同元素
            words.remove(word)
        b.append([word, count])  # 存起来,count为该单词出现次数
    # print(b)
    # 获取b中数字的个数 后面进行排序
    array = []
    for i in range(len(b)):
        array.append(b[i][1])

    array.sort(reverse=True)
    return array, b


# 打印
def print_result(array, b):
    result = []
    for n in list(reversed(list(set(array)))):  # 集合去重打印
        for i in range(len(b)):
            if b[i][1] == n:
                # print("{}出现{}次".format(b[i][0], n))
                result.append([b[i][0], n])
    return result


# 写入csv文件
def write_csv(result):
    with open("张飞宇_20210629_word_result.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(result)
        f.close()


if __name__ == '__main__':
    a, b = count_words(get_words())
    result = print_result(a, b)
    write_csv(result)


