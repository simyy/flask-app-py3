#!/usr/bin/env python
# coding=utf-8

from core.base import *


class User(db.Model, BaseModel):

    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    appId = Column(String(64))
    mobile = Column(String(64))
    unionId = Column(String(256))
    nickName = Column(String(256))
    avatarUrl = Column(String(1024))
    gender = Column(Integer)
    province = Column(String(128))
    city = Column(String(128))
    country = Column(String(128))
    isDeleted = Column(Integer)

    def __init__(self, appId, unionId, nickName, avatarUrl, gender, province=None, city=None, country=None):
        self.appId = appId
        self.unionId = unionId 
        self.nickName = nickName
        self.avatarUrl = avatarUrl
        self.gender = gender
        self.province = province
        self.city = city
        self.country = country
        self.isDeleted = 0

    def __repr__(self):
        return '<User %s>' % self.id

    @classmethod
    def queryByUnionId(cls, unionId):
        return cls.query.filter_by(unionId=unionId).first()

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()
