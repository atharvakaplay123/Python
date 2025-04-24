import mysql.connector as my
con = my.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_test")

cur = con.cursor()
import time
F=1
while(F==1):
    Roll=str(input('Enter Roll No '))
    Name=str(input('Enter Name '))
    S1=eval(input('Enter Marks of Physics(out of 100)     '))
    S2=eval(input('Enter Marks of Chemistry(out of 100)   '))
    S3=eval(input('Enter Marks of Mathematics(out of 100) '))
    S4=eval(input('Enter Marks of IP/CS(out of 100)       '))
    S5=eval(input('Enter Marks of English(out of 100)     '))
    M=S1+S2+S3+S4+S5
    P=M/5
    Grade='a'
    if(S1<=100 and S2<=100 and S3<=100 and S4<=100 and S5<=100):
        print('Total=',M,'/500')
        print('Percentage=',P,'%')
        if(P>80):
            print("Grade A")
            Grade='A'
        elif(P>70):
            print("Grade B")
            Grade='B'
        elif(P>60):
            print("Grade C")
            Grade='C'
        elif(P>50):
            print("Grade D")
            Grade='D'
        elif(P>30):
            print("Grade E")
            Grade='E'
        elif(P<30):
            print("Fail")
        if(P>30):
            print('Pass')
        time.sleep(1)
        print()
    else:
        print("Enter correct values(MAXIMUM MARKS 100)")       
    sql = (
        "insert into marksheet (Roll_no, Name, Physics, Chemistry, Mathematics, optional, Total, Percentage, Grade)"
        "values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
    query = (Roll, Name, S1, S2, S3, S4, M, P, Grade)
    try:
        cur.execute(sql, query)
        con.commit()
    except:
       conn.rollback()    
    con.close()
time.sleep(20)
