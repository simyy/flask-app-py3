#!/usr/bin/env python
# encoding: utf-8

from core.base import *

class Task(db.Model, BaseModel):
    __tablename__ = 'task'

    id   = Column(Integer, primary_key=True)
    name = Column(String(64)) 

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Task %s>' % self.id
