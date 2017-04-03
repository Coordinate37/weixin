#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint, render_template
from app.utils.utils import check_signature, create_menu, del_menu, Sign
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

@acc.route('/jsapi_auth', methods=['GET', 'POST'])
def jsapi_auth():
    url = request.url
    data = request.values.get('a')
    sign = Sign(url)
    result = sign.sign()
    return url