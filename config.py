#!/usr/bin/env python
# -*- coding: utf-8

WELCOME_TEXT = '谢谢您的关注!'
HELLO_TEXT = '你好'
TEXT_REPLY = """
<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
</xml>
"""
IMAGE_REPLY = """
 <xml>
	 <ToUserName><![CDATA[%s]]></ToUserName>
	 <FromUserName><![CDATA[%s]]></FromUserName>
	 <CreateTime>%s</CreateTime>
	 <MsgType><![CDATA[image]]></MsgType>
	 <PicUrl><![CDATA[%s]]></PicUrl>
	 <MediaId><![CDATA[%s]]></MediaId>
 </xml>
"""
VOICE_REPLY = """
<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[voice]]></MsgType>
	<MediaId><![CDATA[%s]]></MediaId>
	<Format><![CDATA[%s]]></Format>
	<Recognition><![CDATA[腾讯微信团队]]></Recognition>
</xml>
"""
MENU_REPLY = """
<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[%s]]></MsgType>
	<Event><![CDATA[%s]]></Event>
	<EventKey><![CDATA[%s]]></EventKey>
</xml>
"""