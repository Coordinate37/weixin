#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from redis import Redis

app = Flask(__name__)
app.config.from_object('config')

redis = Redis()