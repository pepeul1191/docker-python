# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(
    host='localhost',
    port=8080,
    server='cherrypy',
    debug=True,
    reloader=True)
