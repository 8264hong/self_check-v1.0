#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

class Mysql_Helper():

    def __init__(self):
        self.mysql_conn = pymysql.connect("localhost", "root", "123456", "study", charset='utf8')
        self.cursor = self.mysql_conn.cursor()

    def show_table(self):
        cursor = self.mysql_conn.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'study'")
        return cursor.fetchall()

    def insert_word(self,word,unit):
        for i in word:
            sql = "INSERT INTO {} (word, word_explanation, forget_number, important, pass) VALUES ('{}', '{}', '{}', '{}', '{}')".format(unit,i['word'],i['explanation'],0,0,0)
            try:
                with self.mysql_conn.cursor() as cursor:
                    cursor.execute(sql)
                self.mysql_conn.commit()
            except Exception as e:
                print(e)
                self.mysql_conn.rollback()

    def select_data(self,unit):
        sql = "SELECT * FROM {}".format(unit)
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sql)
                select_result = cursor.fetchall()
                return select_result
        except Exception as e:
            print(e)

    def update(self,table,list):
        for i in list:
            sql = 'UPDATE {} SET forget_number=%s WHERE id = %s;'.format(table)
            result = self.cursor.execute(sql, i)
            print(result)
            self.mysql_conn.commit()

    def update_(self,table,list):
        for i in list:
            sql = 'UPDATE {} SET forget_number=%s,important=%s WHERE id = %s;'.format(table)
            result = self.cursor.execute(sql, i)
            print(result)
            self.mysql_conn.commit()
    def create_table(self,unit):
        sql = 'create table {}(id int not null auto_increment,word varchar(20) not null,word_explanation varchar(50) not null,forget_number smallint,important smallint,pass smallint,primary key(id))default charset=utf8;'.format(unit)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            print("创建数据库成功")
        except Exception as e:
            print("创建数据库失败：case%s" % e)



