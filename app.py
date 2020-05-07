# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from process import transfer_table
from eralchemy.main import render_er, get_table_relationship
import base64
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.get_json()
    print(type(transfer_table(a)))
    render_er(transfer_table(a), 'sss.png')
    print("生成缓存图片")
    with open(r'sss.png', 'rb') as image:
        res = base64.b64encode(image.read())
        print('转换为BASE64')
        os.remove('sss.png')
        print('移除图片')
        return res


@app.route('/dot', methods=['POST'])
def pr_dot():
    a = request.get_json()
    dot = get_table_relationship(transfer_table(a))
    print(dot)
    return dot


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, debug=True)
