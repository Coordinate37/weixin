#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hashlib
import urllib2
from flask import make_response
from app import app, redis

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

def create_menu():
    access_token = get_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
    req = urllib2.Request(url, app.config['MENU_SETTING'])
    response = urllib2.urlopen(req)
    return response

def del_menu():
    access_token = get_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % access_token
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response

def get_token():
    access_token = redis.get('wechat:access_token')
    if not access_token:
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
      app.config['APP_ID'], app.config['APP_SECRET'])
        result = urllib2.urlopen(url).read()
        access_token = json.loads(result).get('access_token')
        redis.set('wechat:access_token', access_token, 7200)
    return access_token