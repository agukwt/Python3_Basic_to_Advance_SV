#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mysql.connector


# DBの接続
# conn = mysql.connector.connect(
#     host='localhost', user='root', password='OWN_PASSWORD')
# # 本物のIPアドレスを入れると設定してないのでErrorになる。
#
# cursor = conn.cursor()
#
# cursor.execute('CREATE DATABASE test_mysql_database')
# cursor.close()
# conn.close()

# Tableの作成
# conn = mysql.connector.connect(
#     host='localhost', database='test_mysql_database',
#     user='root', password='OWN_PASSWORD')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#               'id int NOT NULL AUTO_INCREMENT,'
#               'name varchar(14) NOT NULL,'
#               'PRIMARY KEY(id))')
# conn.commit()
# cursor.close()
# conn.close()

# 行の挿入
# conn = mysql.connector.connect(
#     host='localhost', database='test_mysql_database',
#     user='root', password='OWN_PASSWORD')
# cursor = conn.cursor()
# cursor.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# cursor.execute('SELECT * FROM persons')
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()

# 行の更新と削除
# cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
# cursor.execute('DELETE FROM persons WHERE name = "Mike"')

# MySQLでの確認
# show databases;
# use test_mysql_database;