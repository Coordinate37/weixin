#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint
from ..utils import check_signature
from ..response import recv_msg, submit_msg
from . import acc

@acc.route('/weixin', methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        return check_signature(request.args)
    else:
        xmldict = recv_msg(request.data)
        reply = submit_msg(xmldict)
        response = make_response(reply)
        response.content_type = 'application/xml'
        return response