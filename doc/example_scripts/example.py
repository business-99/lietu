#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

名称：运维脚本模型！v0.1
日期：2018-01-25
@author: Tim.Wells

注意点：
   1. quick start, 单库单sql模式。 写好sql及where条件(格式：{})即可。
   2. 多库、多sql模式，import数据库引擎，重写函数trace，并把想要返回的结果正确return即可，注意最后必须关闭数据库连接。
   3. 后台上传，请填写详细信息，包括分组，上传者，脚本名称，脚本描述，脚本文件，[关联DB信息]。
   4. 注意后台权限。

"""
from lietu.master import Canine
# import pymysql
# import cx_Oracle

class Dog(Canine):
    sql = "SELECT * FROM item WHERE id='{}'"

    # def trace(self, order_id):
    #     conn = None
    #     sql = "SELECT status FROM table WHERE order_id='{}'"
    #     try:
    #         db_info = 'sms/sms@host:port/database'
    #         conn = cx_Oracle.connect(db_info)
    #         c = conn.cursor()
    #         c.execute(sql.format(order_id))
    #         result = c.fetchall()
    #     finally:
    #         if conn:
    #             conn.close()
    #     return result
