#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint, render_template
from app.utils.utils import check_signature, create_menu, del_menu, sign
from app.utils.response import wechat_response
from app import app
from . import acc

@acc.route('', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    del_menu()
    create_menu()
    reply = wechat_response(request.data)
    response = make_response(reply)
    response.content_type = 'application/xml'
    return response

@acc.route('/index', methods=['GET', 'POST'])
def index():
    config = sign.sign()
    config['debug'] = True
    config['appId'] = app.config['APP_ID']
    config['jsApiList'] = [
        'onMenuShareTimeline',
        'onMenuShareAppMessage'
    ]
    return render_template('test.html', test='haha', config=config)

@acc.route('/test', methods=['GET', 'POST'])
def test2():
    return render_template('test2.html', test='haha')