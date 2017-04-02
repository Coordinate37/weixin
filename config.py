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
MENU_SETTING = """
{
    "button": [
        {
            "type": "click",
            "name": "今日歌曲",
            "key": "V1001_TODAY_MUSIC"
        },
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": "搜索",
                    "url": "http://www.soso.com/"
                },
                {
                    "type": "view",
                    "name": "视频",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "赞一下我们",
                    "key": "V1001_GOOD"
                }]
        }]
}
"""
