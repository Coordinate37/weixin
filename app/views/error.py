#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import err

@err.route('/error')
def error():
	return 'Error!'