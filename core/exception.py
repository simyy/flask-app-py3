#!/usr/bin/env python
# coding=utf-8

class BaseException(Exception):

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.code)
