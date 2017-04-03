#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

err = Blueprint('err', __name__, url_prefix="/weixin")
acc = Blueprint('acc', __name__, url_prefix="/weixin")