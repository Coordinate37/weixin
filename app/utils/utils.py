#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

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