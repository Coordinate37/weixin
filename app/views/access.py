#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from flask import request, make_response, Blueprint

acc = Blueprint('acc', __name__)

def log(data):
    try:
        fout = open('out.txt')
        fout.write(data)
        fout.close()
    except IOError:
        pass
    except Exception:
        pass

@acc.route('/')
def index():
    return "Hello World!"

@acc.route('/weixin', methods=['GET','POST'])
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
        return 'Token validate failed!'
    log(request.data)
    return request.data

if __name__ == '__main__':
    acc.run(host='0.0.0.0', debug=True)
