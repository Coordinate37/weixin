#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import err

@err.errorhandler(404)
def page_not_found(error):
	return "page not found!", 404

@err.errorhandler(Exception)
def unhandled_exception(error):
	app.logger.error('Unhandled Exception: %s', (error))
	return 'Error', 500