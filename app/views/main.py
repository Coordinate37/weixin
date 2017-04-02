#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint
from app.utils.check_sign import check_signature
from app.utils.response import wechat_response
from . import acc

@acc.route('/weixin', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    reply = wechat_response(request.data)
    response = make_response(reply)
    response.content_type = 'application/xml'
    return response