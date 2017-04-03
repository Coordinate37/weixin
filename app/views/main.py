#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, make_response, Blueprint, jsonify, render_template
from app.utils.utils import check_signature, create_menu, del_menu, get_signature
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
    #url = request.values.get('url')
    url = request.values.get("name")
    print url
    sign = Sign(url)
    result = sign.sign()
    result['appId'] = app.config['APP_ID']
    return jsonify(result)

@acc.route('/share.html', methods=['GET'])
def get():
    print request.url
    signature = get_signature(request.url)
    params = dict(title="微信分享尝试",
                  link="http://newbbs.bingyan.net/topics",
                  imgUrl="http://whbbingyan.cn/team1_1.png",
                  desc="微信自定义分享测试",
                  appId=app.config['APP_ID']
                  )
    params.update(signature)
    params['timestamp'] = str(params['timestamp'])
    # transform params.values from utf-8 to unicode
     
    return render_template('share.html', 
                            title=params['title'],
                            link=params['link'],
                            imgUrl=params['imgUrl'],
                            desc=params['desc'],
                            appId=params['appId'],
                            signature=params['signature'],
                            nonceStr=params['nonceStr'],
                            timestamp=params['timestamp']
                            )