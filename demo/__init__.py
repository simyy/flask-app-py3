#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

demo = Blueprint('demo',
                 __name__)
                 #template_folder='templates',
                 #static_folder='static')

from .views.index import *
