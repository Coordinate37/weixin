#!/usr/bin/env python
# -*- coding: utf-8

WELCOME_TEXT = '谢谢您的关注!'
HELLO_TEXT = '你好'
TEST_TEXT = 'hhhh'
APP_ID = 'wx70078936c4e3f0ce'
APP_SECRET = '74932d08df7577b583972e88446a60a9'
SHARE_URL = 'http://118.89.42.70/weixin/index'
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
NEWS_REPLY = """
<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>%s</ArticleCount>
    <Articles>%s</Articles>
</xml> 
"""
NEWS_ITEM = """
<item>
    <Title><![CDATA[%s]]></Title> 
    <Description><![CDATA[%s]]></Description>
    <PicUrl><![CDATA[%s]]></PicUrl>
    <Url><![CDATA[%s]]></Url>
</item>
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
            "name": "网页",
            "sub_button": [
                {
                    "type": "view",
                    "name": "自定义分享",
                    "url": "http://whbbingyan.cn/weixin/share.html"
                }]
        },
        {
            "name": "Click",
            "sub_button": [
                {
                    "type": "click",
                    "name": "Bingyan",
                    "key": "bingyan"
                },
                {
                    "type": "click",
                    "name": "Teams",
                    "key": "Group"
                }]
        }]
}
"""
# [title, description, picurl, url]
NEWS_CONTENT1 = (
    ("Bingyan", "Bingyan bbs", r"http://www.bingyan.net/static/img/team1_1.png", r"newbbs.bingyan.net"),
)
NEWS_CONTENT2 = (
    ("Bingyan", "Bingyan bbs", r"http://www.bingyan.net/static/img/team1_1.png", r"newbbs.bingyan.net"),
    ("Dian", "Dian 团队官网", r"http://dian.hust.edu.cn/cn/show/slide/1.jpg", r"http://dian.hust.edu.cn/"),
    ("联创团队", "联创团队百科", r"http://www.hustunique.com/static/src/pic/intropage/1.jpg", r"http://baike.baidu.com/item/%E8%81%94%E5%88%9B%E5%9B%A2%E9%98%9F/2148447")
)