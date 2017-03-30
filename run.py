#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from app.views.error import err
from app.views.access import acc

def config_blueprints(app):
	app.secret_key = 'whb'
	blueprints = (err, acc)
	for key in blueprints:
		app.register_blueprint(key)

config_blueprints(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)