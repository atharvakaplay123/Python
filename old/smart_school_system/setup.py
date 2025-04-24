import mysql.connector as my
con=my.connect(
    host='localhost',
    user='root',
    passwd='root',
    )
cur=con.cursor()
cur.execute('create database python')
con=my.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='python'
    )
cur=con.cursor()
