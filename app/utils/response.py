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
        msgtype = xmldata.find('Event').text

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
#    content = xmldata.find('Content').text + app.config['HELLO_TEXT']
#    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)
    itemXml = []
    for article in app.config['NEWS_CONTENT']:
        item = app.config['NEWS_ITEM'] % article
        itemXml.append(item)
    return app.config['NEWS_REPLY'] % (fromusername, tousername, int(time.time()), len(app.config['NEWS_CONTENT']), ''.join(itemXml))

@set_msg_type('subscribe')
def subscribe_resp():
    content = app.config['WELCOME_TEXT']
    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)

@set_msg_type('voice')
def voice_resp():
    content = xmldata.find('Recognition').text
    return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)