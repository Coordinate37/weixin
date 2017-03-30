#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from flask import request, make_response, Blueprint

acc = Blueprint('acc', __name__)

def check_signature(data):
    token = '1997117'
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    echostr = data.get('echostr', '')
    s = [timestamp, nonce, token]
    s.sort()
    s = ''.join(s)
    if(hashlib.sha1(s).hexdigest() == signature):
        return make_response(echostr)
    else:
        return "Access failed!"

@acc.route('/weixin', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    else:
        return "Post!"

if __name__ == '__main__':
    acc.run(host='0.0.0.0', debug=True)
