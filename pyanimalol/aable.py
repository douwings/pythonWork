# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:wing1020@127.0.0.1:3306/pytest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
 
db = SQLAlchemy(app)  # 实例化
 
 
# 数据模型设计
# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(30), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个人简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标志
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关联
    comments = db.relationship('Comment', backref='user')  # 电影评论外键关联
    moviecols = db.relationship('Moviecol', backref='user')  # 电影收藏外键关联
 
    def __repr__(self):
        return "<User %r>" % self.name
 
 
# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 最近登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间
 
    def __repr__(self):
        return "<Userlog %r>" % self.id
 
 
# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    movies = db.relationship("Movie", backref='tag')  # 电影外键关联
 
    def __repr__(self):
        return "<Tag %r>" % self.name
 
 
# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 时长
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    comments = db.relationship("Comment", backref='movie')  # 评论外键关联
    moviecols = db.relationship('Moviecol', backref='movie')  # 电影收藏外键关联
 
    def __repr__(self):
        return "<Movie %r>" % self.title
 
 
# 电影预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
 
    def __repr__(self):
        return "<Preview %r>" % self.title
 
 
# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
 
    def __repr__(self):
        return "<Comment %r>" % self.id
 
 
# 收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
 
    def __repr__(self):
        return "<Moviecol %r>" % self.id
 
 
# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
 
    def __repr__(self):
        return "<Auth %r>" % self.name
 
 
# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(1000), unique=True)  # 权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
 
    def __repr__(self):
        return "<Role %r>" % self.name
 
 
# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否是超级管理员,0为超级管理员,1不是
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    adminlogs = db.relationship("Adminlog", backref='admin')  # 管理员登录日志外键关联
    oplogs = db.relationship("Oplog", backref='admin')  # 管理员操作日志外键关联
 
    def __repr__(self):
        return "<Admin %r>" % self.name
 
 
# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 最近登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间
 
    def __repr__(self):
        return "<Adminlog %r>" % self.id
 
 
# 后台操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 最近登录ip
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间
 
    def __repr__(self):
        return "<Oplog %r>" % self.id
 
 
db.create_all()