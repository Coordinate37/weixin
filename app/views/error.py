#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

err = Blueprint('err', __name__)

@err.route('/error')
def error():
	return 'Error!'