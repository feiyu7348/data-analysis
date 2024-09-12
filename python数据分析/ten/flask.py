#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_worde():
    return 'Hello Worde'

if __name__ == '__main__':
    app.run()