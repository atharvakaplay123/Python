import mysql.connector as my
con = my.connect(host="localhost", port=3306, user="root",password="root", database="school")
cur = con.cursor()
query = "desc stu_data"
cur.execute(query)
for x in cur:
    print(x)
con.close()
