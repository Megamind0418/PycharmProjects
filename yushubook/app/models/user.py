"""
Created by 张 on 2019/8/20 
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

__author__ = '张'


# 用户模型类
# UserMiXin flask_login 插件中的一个可以表明用户身份的类
# 比如 get_id 函数,login_user 将用户票据写入 cookie 时,表明只写入 id 这个可以表明用户身份的属性
class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        """
        password属性读取
        :return:
        """
        return self._password

    @password.setter
    def password(self, raw):
        """
        password属性写入
        :param raw: 原始password
        """
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """
        检查原密码和数据库密码哈希值
        :param raw: 原密码
        :return: 检查原密码和数据库密码哈希值的结果
        """
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        """
        用户是否能将书籍加入心愿清单或者赠送清单
        :param isbn: 书籍 isbn
        :return:
        """
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 查询 Gift.Wish 模型,查询参数为 uid,isbn,launched
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        # 既不在赠送清单,也不在心愿清单才能添加
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    """
    User 模型里，编写 get_user 方法用来根据 id 查询用户，并加入 @login_manager.user_loader 装饰器
    加上装饰器 flask_login 才知道调用此函数
    :param uid: 用户 id
    :return:用户模型
    """
    return User.query.get(int(uid))
