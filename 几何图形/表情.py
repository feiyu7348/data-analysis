#!/usr/bin/env python
# -*- coding:utf-8 -*-

import emoji

result1 = emoji.emojize(':thumbs_up:')  # 👍
print(result1)

# 有些特殊的表情需要指定 use_aliases=True 参数才可以实现
result2 = emoji.emojize(':zzz:', use_aliases=True)  # 💤
print(result2)

# 同时也支持反向操作
# 脑阔疼 :hear-no-evil_monkey:
print(emoji.demojize('脑阔疼 🙉')) 
