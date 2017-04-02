#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint
from app.utils.utils import check_signature, init_wechat
from app.utils.response import wechat_response
from . import acc

@acc.route('/weixin', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    init_wechat()
    reply = wechat_response(request.data)
    response = make_response(reply)
    response.content_type = 'application/xml'
    return response