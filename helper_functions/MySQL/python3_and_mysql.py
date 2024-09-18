# -*- coding: utf-8 -*-
"""
The given code provides a way to connect to mysql using python3.

package used - pymysql
command to install - pip3 install pymysql
"""

import pymysql

# conn = pymsql.connect("host", "username", "password", "db_name")
conn = pymysql.connect("0.0.0.0", "username", "password", "db_name")
x = conn.cursor()

ONE = 1
first_name = 'Abhinav'
last_name = 'Singh'
addr = 'address'
age = 18

# SELECT QUERY
sql = """SELECT * FROM `user_details` WHERE `first_name`='%s'""" % (first_name)
x.execute(sql)
li = list()
for i in x.fetchall():
    li.append(i)


# another way to execute the sql query
sql = """SELECT * FROM `user_details` WHERE `first_name`=%s"""
x.execute(sql, [first_name])
li = list()
for i in x.fetchall():
    li.append(i)


# INSERT QUERY
"""
we use %s for all fields while inserting data as the format string is not
really a normal python format string.
"""
sql = """INSERT INTO user_details (`first_name`,`last_name`, `age`,
         `address`) VALUES (%s, %s, %s, %s)"""
x.execute(sql, [first_name, last_name, age, addr])
conn.commit()

# UPDATE QUERY
sql = """UPDATE user_details SET age = '%s'
         WHERE first_name='%s'""" % (age, first_name)
x.execute(sql)
conn.commit()


# DELETE QUERY THAT WILL DELETE ALL RECORDS THAT WERE CREATED 10 MINUTE'S AGO
sql = 'DELETE FROM test WHERE time <= NOW()- INTERVAL 10 MINUTE'
x.execute(sql)
conn.commit()
