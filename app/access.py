#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from flask import Flask, request, make_response

from auth import acc

@acc.route('/')
def index():
    return "Hello World!"

@acc.route('/weixin',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        print 'coming Get'
        data = request.args
        token = "1997117"
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
        return '1000'
        return make_response(echostr)
    return '404 Not Found!hahaha'
# from flask import Flask, request, make_response

# acc = Flask(__name__)

# @acc.route('/', methods=['GET', 'POST'])
# def index():
#     print request.method
#     if request.method == 'GET':
#         data = request.args
#         echostr = data.get('echostr', '')
#         return make_response(echostr)
#     return 'hahaha'

if __name__ == '__main__':
    acc.run(host='0.0.0.0', debug=True)
