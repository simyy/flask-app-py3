#!/usr/bin/env python
# encoding: utf-8

from flask import render_template

from .. import demo

@demo.app_errorhandler(404)
def page_not_found(e):
    return "page not found"


@demo.app_errorhandler(500)
def internal_server_error(e):
    return "internal server error"
