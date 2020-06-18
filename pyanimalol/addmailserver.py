# coding=utf-8
# from Flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
import json

test = []
app = Flask(__name__)
# 配置数据库的地址URI , 格式 "数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名"  , 端口号可以不写.
# python3中用的mysql驱动是mysql-connector , 已经不支持python2的MySQLdb驱动.
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:wing1020@127.0.0.1:3306/pytest"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://animalol:c9ad72c6-4862-44b8-90d3-e2875692d70e@rds.teeqee.com:33330/animalol"
# 跟踪数据库的修改 --> 不建议开启 , 一是消耗性能 , 二是未来的版本中会移除.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 将app作为参数传入这个关联工具 , 创建一个两者相关联对象db
db = SQLAlchemy(app)
# print(app.config)


class Gamer(db.Model):
    __tablename__ = "gamer"
    uid = db.Column(db.String(255))
    openid = db.Column(db.String(100), unique=True, primary_key=True)
    gold = db.Column(db.Integer)
    diamond = db.Column(db.Integer)
    nickname = db.Column(db.String(255))

    def __repr__(self):
        """返回定制对象输出信息 , 与__str__作用类似"""
        return "User:%s %s %s %s %s" % (self.uid, self.openid, self.gold, self.diamond, self.nickname)


class Mail(db.Model):
    __tablename__ = "mail"
    dataid = db.Column(db.Integer, unique=True, primary_key=True)
    gmtype = db.Column(db.Integer)
    uid = db.Column(db.String(255))
    reward = db.Column(db.String(500))

    def __repr__(self):
        """返回定制对象输出信息 , 与__str__作用类似"""
        return "Mail:%s %s %s %s" % (self.dataid, self.gmtype, self.uid, self.reward)
        # return "Mail:%s %s" % (self.uid, self.reward)


@app.route('/wings')
def wings():
    gamer = Gamer.query.all()
    # print(gamer)
    return render_template('index.html', name=gamer)


@app.route('/userfind', methods=['POST', 'GET'])
def bio_data_userfind():
    print("userinfor", request.method)
    if request.method == "POST":
        nickname = request.form['nickname']
        # gamerone = Gamer.query.filter(Gamer.nickname == nickname).first()
        return redirect(url_for('userinfor',
                                nickname=nickname,))
    return render_template("userfind.html")


@app.route('/userinfor', methods=['GET'])
def userinfor():
    print("userinfor")
    print(request.args)
    nickname = request.args.get('nickname')

    # 查询该玩家
    gamerone = Gamer.query.filter(Gamer.nickname == nickname).first()
    print(gamerone)
    return render_template("userinfor.html",
                           nickname=gamerone.nickname,
                           gold=gamerone.gold,
                           diamond=gamerone.diamond,)


@app.route('/form', methods=['POST', 'GET'])
def bio_data_form():
    if request.method == "POST":
        nickname = request.form['nickname']
        GMtype = request.form['GMtype']
        gold = request.form['gold']
        diamond = request.form['diamond']
        # gamerone = Gamer.query.filter(Gamer.nickname == nickname).first()
        return redirect(url_for('showbio',
                                nickname=nickname,
                                gold=gold,
                                diamond=diamond,))
    return render_template("bio_form.html")


@app.route('/showbio', methods=['GET'])
def showbio():
    print("showbio")
    print(request.args)
    nickname = request.args.get('nickname')
    GMtype = request.args.get('GMtype')
    gold = request.args.get('gold')
    diamond = request.args.get('diamond')

    # 查询该玩家并修改
    gamerone = Gamer.query.filter(Gamer.nickname == nickname).first()
    print(gamerone)
    uid = gamerone.uid
    reward = [1, 1]
    reward[0] = int(gold)
    reward[1] = int(diamond)
    reward_json = json.dumps(reward)
    print(reward_json)
    beforgold = int(gamerone.gold)
    befordiamond = int(gamerone.diamond)
    gamerone.gold = int(gamerone.gold) + int(gold)
    gamerone.diamond = int(gamerone.diamond) + int(diamond)

    mail = Mail(uid=uid, gmtype=GMtype,  reward=reward_json)
    print(mail)
    db.session.add(mail)

    db.session.commit()

    return render_template("show_bio.html",
                           nickname=gamerone.nickname,)


if __name__ == '__main__':
    app.run(debug=True, port=19989)
