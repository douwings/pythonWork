# coding:utf-8
"""
@author:ZouLingyun
@date: 2019/12/9
@summary:
    数据库表结构同步
"""
import copy
import re
import sys

import pandas as pd
from loguru import logger
from sqlalchemy import create_engine


class Cons(object):
    base_cons = 'mysql+pymysql://{user}:{password}@{host}:{port}'

    def __init__(self, user, password, port, host, comments):
        self.cons = self.base_cons.format(user=user, password=password, port=port, host=host)
        self.comments = comments


class DbConnections(object):
    # 深圳 rds
    prod_sz_rds = Cons(user='root', password='zhiyun_mysql3307', port=3306,
                       host='rm-wz9dzy9fiq6xg4hfmao.mysql.rds.aliyuncs.com', comments="深圳 rds 数据库")

    # 深圳 ecs 安装 mysql 3307 端口
    prod_sz_ecs_3307 = Cons(user='root', password='zhiyun.mysql3307', port=3307, host='112.74.181.143',
                            comments="深圳 ecs 安装 mysql 3307 端口")

    # 杭州 ecs 安装 mysql 3306 端口
    test_hz_ecs_3306 = Cons(user='root', password='root', port=3306, host='47.99.180.185',
                            comments="杭州 ecs 安装 mysql 3306 端口")

    # 备份服务器 172.16.2.101:3306
    backup_101 = Cons(user='root', password='root', port=3306, host='172.16.2.101', comments="备份服务器 172.16.2.101:3306")

    # # 本地虚拟机数据库
    # local_virtual_db = Cons(user='root', password='Gb16chng!', port=3306, host='192.168.80.2', comments="本地虚拟机数据库")


class SyncDb(object):
    def __init__(self, src_db_cons: str, dest_db_cons: str):
        """

        :param src_db_cons: 源数据库连接串
        :param dest_db_cons: 目标数据库连接串
        """
        msg = "需要提供数据库连接串: {}/db_schema".format(Cons.base_cons)
        assert bool(src_db_cons), msg
        assert bool(dest_db_cons), msg
        self.src_schema = src_db_cons.rsplit('/', 1)[1]
        self.dest_schema = dest_db_cons.rsplit('/', 1)[1]
        self._src_db_cons = src_db_cons
        self._dest_db_cons = dest_db_cons
        self.src_db_engine, self.dest_db_engine = self._get_engine()

    def run(self, target_tabs: list = None, create_tab=False):
        """
        同步数据库表结构
        :param target_tabs: 同步目标表，如果不指定，则同步目标 schema 下所有表
        :param create_tab: 是否创建表
        :return: None
        """
        src_tabs = self._get_src_tabs(target_tabs)

        for tab in src_tabs:
            if_create_tab, create_sql = self._comp_tab_sql(tab)
            if if_create_tab:
                create_sql = self._proc_auto_increment(create_sql)
                create_sql = self._replace_space(create_sql)
                if create_tab:
                    self.dest_db_engine.execute(create_sql)
                    logger.info("迁移表结构: {}".format(tab))
                else:
                    logger.info("扫描到表: {}".format(tab))
            else:
                logger.debug("不迁移表结构，该表已经存在: {}".format(tab))
            logger.debug('==' * 20)

    def _comp_tab_sql(self, table_name):
        """
        比较源库和目标库表
        :param table_name: 数据库表名
        :return: bool, True: 需要创建表， False: 不需要创建表
        """
        show_create_sql = "show create table {tab}".format(tab=table_name)
        src_create_tab_sql = pd.read_sql(show_create_sql, con=self.src_db_engine)['Create Table'].tolist()[0]

        dest_exist_sql = """
        SELECT table_name from information_schema.tables where table_schema='{schema}'  and table_name='{tab}'
        """.format(schema=self.dest_schema, tab=table_name)
        df = pd.read_sql(dest_exist_sql, con=self.dest_db_engine)
        if df.empty:
            return True, src_create_tab_sql
        else:
            dest_create_tab_sql = pd.read_sql(show_create_sql, con=self.dest_db_engine)['Create Table'].tolist()[0]

        src_sql_seq = self._parse_create_tab_sql(src_create_tab_sql)
        dest_sql_seq = self._parse_create_tab_sql(dest_create_tab_sql)

        src_sql_seq = [self._drop_comments(s) for s in src_sql_seq]
        dest_sql_seq = [self._drop_comments(s) for s in dest_sql_seq]

        if src_sql_seq == dest_sql_seq:
            return False, src_create_tab_sql
        else:
            logger.warning(
                "迁移的表: {tab}, 已经在目标库: {dest_schema} 存在，且结构与源库不同".format(tab=table_name, dest_schema=self.dest_schema))
            src_diff_dest = list(set(src_sql_seq) - set(dest_sql_seq))
            src_diff_dest.sort()
            dest_diff_src = list(set(dest_sql_seq) - set(src_sql_seq))
            dest_diff_src.sort()
            if bool(src_diff_dest) or bool(dest_diff_src):
                logger.warning("源表字段与目标表字段差集  : \n{}".format('\n'.join(src_diff_dest)))
                logger.warning("目标表字段与源表字段差集: \n{}".format('\n'.join(dest_diff_src)))
        return False, src_create_tab_sql

    @classmethod
    def _drop_comments(cls, sql):
        """出去sql语句中的 comment 信息"""
        pattern = re.compile(r' +comment +\S+', re.IGNORECASE)
        sql = pattern.sub(",", sql)
        return sql.replace(',', '')

    @classmethod
    def _proc_auto_increment(cls, tab_sql: str):
        """
        去除 AUTO_INCREMENT
        :param tab_sql: 建表语句
        :return:
        """
        pattern = re.compile(r'auto_increment\s*=\s*\d+', re.IGNORECASE)
        sql = pattern.sub('', tab_sql)
        return sql

    @classmethod
    def _replace_space(cls, tab_sql: str):
        """
        将多个空格替换成一个空格
        :param tab_sql: 建表语句
        :return:
        """
        pattern = re.compile(r' +')
        sql = pattern.sub(' ', tab_sql)
        return sql

    def _parse_create_tab_sql(self, create_tab_sql: str):
        """拆解建表语句，用于比较两张表结构是否一样"""
        sql = self._proc_auto_increment(create_tab_sql)
        sql = self._replace_space(sql)
        sql = sql.lower()
        sql_seq = [r.strip() for r in sql.split('\n') if r.strip()]
        sql_seq.sort()
        return sql_seq

    def _get_src_tabs(self, target_tabs: list = None):
        """
        扫描源数据库获取表名，如果指定目标表则检测指定的表是否存在
        :param target_tabs: 数据库表名列表
        :return:
        """
        if target_tabs is None:
            sql_target_tabs = list()
            target_tabs = list()
        else:
            sql_target_tabs = copy.deepcopy(target_tabs)
        assert isinstance(sql_target_tabs, list), "target_tabs 传入数据需要是 list"
        if len(sql_target_tabs) == 1:
            t_sql = """
            SELECT table_name from information_schema.tables where table_schema='{schema}'  and table_name='{tab}'
            """.format(schema=self.src_schema, tab=sql_target_tabs[0])
        elif sql_target_tabs:
            sql_target_tabs = tuple(['{}'.format(t) for t in sql_target_tabs])
            t_sql = """
            SELECT table_name from information_schema.tables where table_schema='{schema}' and table_name in {tabs}
            """.format(schema=self.src_schema, tabs=sql_target_tabs)
        else:
            t_sql = """
            SELECT table_name from information_schema.tables where table_schema='{schema}'
            """.format(schema=self.src_schema)

        src_db_tabs = pd.read_sql(sql=t_sql, con=self._src_db_cons)['table_name'].tolist()
        diff_tabs = list(set(target_tabs) - set(src_db_tabs))
        if diff_tabs:
            logger.warning("以下目标表不在源数据库中:\n{}".format('\n'.join(diff_tabs)))
        return src_db_tabs

    def _get_engine(self):
        return create_engine(self._src_db_cons), create_engine(self._dest_db_cons)


def get_con_obj():
    """获取数据库连接对象"""
    con_objs = [getattr(DbConnections, w) for w in dir(DbConnections) if isinstance(getattr(DbConnections, w), Cons)]
    return con_objs


def choice_db():
    digit_pattern = re.compile(r'\s*\d+\s*')
    con_objs = get_con_obj()
    comments = [o.comments for o in con_objs]
    for i, c in enumerate(comments):
        print(i, c)
    src_choice = input("输入编号 >>>")
    src_choice = digit_pattern.fullmatch(src_choice)
    if src_choice:
        src_choice_index = int(src_choice.group())
        if src_choice_index not in list(range(len(con_objs))):
            print("没有选择数据库，退出程序")
            sys.exit(0)
        db = con_objs[src_choice_index]
        return db
    else:
        print("没有选择数据库，退出程序")
        sys.exit(0)


def default_run():
    # TODO 朱爷
    src_cons = DbConnections.backup_101.cons + '/zy'
    dest_cons = DbConnections.test_hz_ecs_3306.cons + '/zy'

    tabs = ['product_params']
    # tabs = None
    sd = SyncDb(src_db_cons=src_cons, dest_db_cons=dest_cons)
    sd.run(tabs, create_tab=True)


def main():
    main_choice = input("1 按照默认信息同步表\n2 引导模式同步表\n>>>").strip()
    if main_choice == '1':
        default_run()
    elif main_choice == '2':
        print("选择源数据库")
        src_db = choice_db()
        print('==' * 20)
        print('选择目标数据库')
        dest_db = choice_db()

        src_schema = input("输入源数据库 schema >>>").strip()
        dest_schema = input("输入目标数据库 schema >>>").strip()

        if not src_schema.startswith('/'):
            src_schema = '/' + src_schema
        if not dest_schema.startswith('/'):
            dest_schema = '/' + dest_schema

        if_create_tab = input("是否迁移表，默认不迁移，输入(y/n)>>>")
        if_create_tab = if_create_tab.lower() == 'y'
        sd_obj = SyncDb(src_db_cons=src_db.cons + src_schema, dest_db_cons=dest_db.cons + dest_schema)
        sd_obj.run(create_tab=if_create_tab)
    else:
        print("没有输入选项，程序退出")
        sys.exit(0)


if __name__ == '__main__':
    main()
    # default_run()
