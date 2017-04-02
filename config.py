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
                    "url": "http://www.baidu.com/"
                },
                {
                    "type": "view",
                    "name": "视频",
                    "url": "http://v.qq.com/"
                }]
        }]
}
"""
# [title, description, picurl, url]
NEWS_CONTENT = (
    ("Bingyan", "Bingyan bbs", r"http://www.bingyan.net/static/img/team1_1.png", r"newbbs.bingyan.net"),
    ("Dian", "Dian 团队官网", r"http://dian.hust.edu.cn/cn/show/slide/1.jpg", r"http://dian.hust.edu.cn/"),
    ("联创团队", "联创团队百科", r"http://www.hustunique.com/static/src/pic/intropage/1.jpg", r"http://baike.baidu.com/item/%E8%81%94%E5%88%9B%E5%9B%A2%E9%98%9F/2148447")
)