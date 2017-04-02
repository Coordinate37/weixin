#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import xml.etree.ElementTree as ET
import sys
from app import app

reload(sys)
sys.setdefaultencoding('utf-8')

msg_type_resp = {}

def wechat_response(data):
    global xmldata, fromusername, tousername, msgtype

    xmldata = ET.fromstring(data)
    fromusername = xmldata.find('FromUserName').text
    tousername = xmldata.find('ToUserName').text
    msgtype = xmldata.find('MsgType').text
    if msgtype == 'event':
        msgtype = 'event:%s' % xmldata.find('Event').text

    try:
        get_resp_func = msg_type_resp[msgtype]
        response = get_resp_func()
    except KeyError:
        response = 'success'

    return response

def set_msg_type(msg_type):
    """
    msg_type=>function decorator
    """
    def decorator(func):
        msg_type_resp[msg_type] = func
        return func
    return decorator

@set_msg_type('text')
def text_resp():
   content = xmldata.find('Content').text + app.config['HELLO_TEXT']
   return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)
    

@set_msg_type('event:subscribe')
def subscribe_resp():
    content = app.config['WELCOME_TEXT']
    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)

@set_msg_type('event:voice')
def voice_resp():
    content = xmldata.find('Recognition').text
    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)

@set_msg_type('event:CLICK')
def click_resp():
    content = app.config['WELCOME_TEXT']
    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)
    eventkey = xmldata.find('EventKey').text
    if eventkey == 'Group':
        return news_resp1()
    return news_resp2()

def news_resp1():
    itemXml = []
    for article in app.config['NEWS_CONTENT1']:
        item = app.config['NEWS_ITEM'] % article
        itemXml.append(item)
    return app.config['NEWS_REPLY'] % (fromusername, tousername, int(time.time()), len(app.config['NEWS_CONTENT']), ''.join(itemXml))

def news_resp2():
    itemXml = []
    for article in app.config['NEWS_CONTENT2']:
        item = app.config['NEWS_ITEM'] % article
        itemXml.append(item)
    return app.config['NEWS_REPLY'] % (fromusername, tousername, int(time.time()), len(app.config['NEWS_CONTENT']), ''.join(itemXml))