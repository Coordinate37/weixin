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

@set_msg_type('event')
def event_resp():
	event = xmldata.find('Event').text
	if event == 'subscribe':
		content = app.config['WELCOME_TEXT']
		return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)
	else if event == 'voice':
		content = xmldata.find('Recognition').text
		return app.config['TEXT_REPLY'] % (fromusername, tousername, int(time.time()), content)
	return ''