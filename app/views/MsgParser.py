#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import xml.etree.ElementTree as ET
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def recv_msg(data):
	xmldata = ET.fromstring(data)
	# Sender ID
	fromusername = xmldata.find('FromUserName').text
	# User ID
	tousername = xmldata.find('ToUserName').text
	# Message content
	content = xmldata.find('Content').text
	xmldict = {'FromUserName': fromusername, 'ToUserName': tousername, 'Content': content}
	return xmldict

def submit_msg(content_dict={'': '', type='text'}):
	toname = content_dict['FromUserName']
	fromname = content_dict['ToUserName']
	content = content_dict['Content']
	content = "你好，%s" % (content)
	reply = """
    <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
    </xml>
	"""
    resp_str = reply % (toname, fromname, int(time.time()), content)
    return resp_str