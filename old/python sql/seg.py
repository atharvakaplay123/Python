import mysql.connector
a = int(input('roll'))        
b = str(input("name"))
conn = mysql.connector.connect(
   user='root', password='root', host='localhost', database='test')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO test(roll, name)"
   "VALUES (%s, %s)"
)
data = (a, b)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()
