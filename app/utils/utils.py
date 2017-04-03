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

class Sign(object):
    def __init__(self, url):
        self.appId = app.config['APP_ID']
        self.appSecret = app.config['APP_SECRET']

        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'timestamp': self.__create_timestamp(),
            'jsapi_ticket': self.get_jsapi_ticket(),
            'url': url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def get_access_token(self):
        access_token = redis.get('wechat:access_token')
        if not access_token:
            url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
                app.config['APP_ID'], app.config['APP_SECRET'])
            result = urllib2.urlopen(url).read()
            access_token = json.loads(result).get('access_token')
            redis.set('wechat:access_token', access_token, 7000)
        return access_token

    def get_jsapi_ticket(self):
        jsapi_ticket = redis.get('jsapi_ticket')
        if not jsapi_ticket:
            url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token=%s" % (self.get_access_token())
            result = urllib2.urlopen(url).read()
            jsapi_ticket = json.loads(result).get('ticket')
            redis.set('jsapi_ticket', jsapi_ticket, 7000)
        return jsapi_ticket

    def sign(self):
        signature = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        self.ret['signature'] = hashlib.sha1(signature).hexdigest()
        return self.ret

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