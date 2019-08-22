"""
Created by 张 on 2019/8/8 
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db, Base

__author__ = '张'


# 书籍模型类
class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(100))
