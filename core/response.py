#!/usr/bin/env python
# coding=utf-8

import json
from flask import jsonify
from datetime import datetime
from core.base import JsonSerialize


class Response:
    '''
    Base Response
    '''
    def __init__(self, err, msg, data):
        self.err = err
        self.msg = msg
        self.data = data

    def toJson(self):
        res = {'err': self.err, 'msg': self.msg, 'data': self.data}
        return jsonify(res)


class ErrorResponse(Response):
    '''
    Error Response
    '''
    def __init__(self, err, msg):
        super().__init__(err, msg, None)

    @staticmethod
    def of(err, msg):
        return ErrorResponse(err, msg).toJson()


class SuccessResponse(Response):
    '''
    Success Response
    '''
    def __init__(self, data):
        super().__init__(0, "ok", data)

    @staticmethod
    def of(data):
        if isinstance(data, PagerData):
            data = data.toJson()
        elif isinstance(data, list):
            data = [x.toJson() for x in data]
        elif isinstance(data, JsonSerialize):
            data = data.toJson()
        return SuccessResponse(data).toJson()


class PagerData:
    '''
    Pager Data, data of SuccessResponse
    '''
    def  __init__(self, offset, limit, datas):
        '''
        @offset and @limit is query param
        @datas is data list
        '''
        self.offset = offset
        self.limit = limit
        self.datas = datas
        if self.datas and len(self.datas) > 0:
            self.offset += limit

    def toJson(self):
        return {
                "offset": self.offset,
                "limit": self.limit,
                "list": [x.toJson() for x in self.datas]
               }
