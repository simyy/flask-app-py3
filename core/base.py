#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Text

from .app import db



class JsonSerialize(object):
    """
    JsonSerialize
    """
    def toJson(self):
         record = {}
         # 检索结果集的行记录
         for field in self.__dict__:
             if not field.startswith('_') and hasattr(self.__getattribute__(field), '__call__') == False:
                 data = self.__getattribute__(field)
                 try:
                     record[field] = data
                 except TypeError:
                     record[field] = None
         return record
    


class BaseModel(JsonSerialize):
    """
    Base DB Model
    
    Every table must have isDeleted, then can use the function of query with valid data !!!
    queryAll is the origin query function !!!
    """

    db = db

    def save(self):
        '''dave or update'''
        self.db.session.add(self)
        self.db.session.commit()

    def delete(self, soft=False):
        '''delete by status'''
        if soft:
            self.isDeleted = 1
            self.save()
        else:
            self.db.session.delete(self)
            self.db.session.commit()

    def __str__(self):
        return '<%s %s>' % (type(self).__name__ ,self.id)  

    def __repr__(self):
        return '<%s %s>' % (type(self).__name__ ,self.id)  

    @classmethod
    def deleteById(cls, id, soft=True):
        res = cls.query.filter_by(id=id).first()
        if res:
            res.delete(soft=soft)

    @classmethod
    def query(cls):
        '''query of valid status'''
        return cls.query.filter(cls.isDeleted == 0)

    @classmethod
    def queryAll(cls):
        '''query with delete ones'''
        return cls.query

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def queryByIds(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()
