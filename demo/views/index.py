#!/usr/bin/env python
# encoding: utf-8

from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from manage import app
from .. import demo
from ..models import User
from core.response import SuccessResponse
from core.base import JsonSerialize


@demo.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info(User.query.all())
    return render_template('index.html')


class DemoDTO(JsonSerialize):

    def __init__(self, A, B):
        self.a = A
        self.b = B


@demo.route('/json', methods=['GET'])
def json():
    rs = User.query.all()
    app.logger.info("hello")
    return SuccessResponse.of(rs)
    #return SuccessResponse.of(DemoDTO(1, 1))
