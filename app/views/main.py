#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint
from app.utils.utils import check_signature, create_menu, del_menu
from app.utils.response import wechat_response
from . import acc

@acc.route('/weixin', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    del_menu()
    create_menu()
    reply = wechat_response(request.data)
    response = make_response(reply)
    response.content_type = 'application/xml'
    return response