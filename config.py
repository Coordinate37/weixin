#!/usr/bin/env python
# -*- coding: utf-8

WELCOME_TEXT = '谢谢您的关注!'
HELLO_TEXT = '你好'
TEST_TEXT = 'hhhh'
APP_ID = 'wx70078936c4e3f0ce'
APP_SECRET = '74932d08df7577b583972e88446a60a9'
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
MENU_SETTING = {
    "button": [
        {
            "name": "我是学霸",
            "sub_button": [
                {
                    "type": "click",
                    "name": "期末成绩",
                    "key": "score",
                    "sub_button": []
                },
                {
                    "type": "view",
                    "name": "四六级成绩",
                    "url": "http://115.159.64.43/CETQuery/",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": "一键续借",
                    "key": "renew_books",
                    "sub_button": []
                }
            ]
        },
        {
            "type": "click",
            "name": "Jay Chou",
            "key": "music",
            "sub_button": []
        }
    ]
}
