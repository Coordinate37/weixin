#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
import string
import time
import hashlib
import urllib2
from flask import make_response
from app import app, redis
        
def _create_nonce_str():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
    
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
    access_token = get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
    req = urllib2.Request(url, app.config['MENU_SETTING'])
    response = urllib2.urlopen(req)
    return response

def del_menu():
    access_token = get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % access_token
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response

def get_access_token():
    access_token = redis.get('wechat:access_token')
    if not access_token:
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
      app.config['APP_ID'], app.config['APP_SECRET'])
        result = urllib2.urlopen(url).read()
        access_token = json.loads(result).get('access_token')
        redis.set('wechat:access_token', access_token, 7000)
    return access_token

def get_jsapi_ticket():
    jsapi_ticket = redis.get('jsapi_ticket')
    if not jsapi_ticket:
        url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token=%s" % (get_access_token())
        result = urllib2.urlopen(url).read()
        jsapi_ticket = json.loads(result).get('ticket')
        redis.set('jsapi_ticket', jsapi_ticket, 7000)
    return jsapi_ticket

def get_signature(url):
    timestamp = int(time.time())
    nonceStr = _create_nonce_str()
    url = url
    jsapi_ticket = get_jsapi_ticket()
#    s = "jsapi_ticket=" + js_ticket + "&noncestr=" + noncestr + "&timestamp=" + str(timestamp) + "&url=" + url
    s = "jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s" % (jsapi_ticket, nonceStr, timestamp, url)
    signature = hashlib.sha1(s).hexdigest()
    return dict(timestamp=timestamp, nonceStr=nonceStr, signature=signature, jsapi_ticket=jsapi_ticket)