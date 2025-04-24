import mysql.connector as my
import pandas as py
import matplotlib.pyplot as pl
con=my.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='python'
    )
cur=con.cursor()
asd=0
while(asd==0):
    print()
    print('WELCOME TO SMART STUDENT DATA MANAGEMENT SYSTEM')
    print('Enter the command to proceed.\n Type "insert" to insert single record.\n Type "insert multiple" to multiple records\n Type "view" to view data.\n Type "save" to save data as .csv file.\n Type "delete" to delete a specific record.\n Type "delete multiple" to delete a multiple records.\n Type "delete all" to clear whole data.\n Type "plot age" to plot age graph.\n Type "exit" to exit the software.')
    a=str(input('Enter command:'))
    if (a=="insert"):
        roll=[]
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            roll.append(a)
        Roll_No=int(input('Roll NO: '))
        while(Roll_No<1000 or Roll_No>10000):
            print("Roll No should be 4 digit")
            Roll_No=int(input('Roll NO: '))
        for m in roll:
            while(m==Roll_No):
                print("Roll No Repeted, Please try again")
                Roll_No=int(input('Roll NO: '))  
        Name=str(input('Name: '))
        Age=int(input('Age: '))
        query=('insert into test(Roll_No,Name,Age)''values(%s,%s,%s)')
        values=(Roll_No,Name,Age)
        cur.execute(query,values)
        print('SAVED TO DATABASE')
    elif (a=="insert multiple"):
        n=int(input("no of entries"))
        for i in range(0,n,1):
            roll=[]
            cur.execute('select * from test')
            for i in cur:
                (a,b,c)=i
                roll.append(a)
            Roll_No=int(input('Roll NO: '))
            while(Roll_No<1000 or Roll_No>10000):
                print("Roll No should be 4 digit")
                Roll_No=int(input('Roll NO: '))
            for m in roll:
                while(m==Roll_No):
                    print("Roll No Repeted, Please try again")
                    Roll_No=int(input('Roll NO: '))
            Name=str(input('Name: '))
            Age=int(input('Age: '))
            query=('insert into test(Roll_No,Name,Age)''values(%s,%s,%s)')
            values=(Roll_No,Name,Age)
            cur.execute(query,values)
            print('SAVED TO DATABASE')
    elif (a=="view"):
        roll=[]
        name=[]
        age=[]
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            roll.append(a)
            name.append(b)
            age.append(c)
        df=py.DataFrame()
        df["Roll_No"]=roll
        df["Name"]=name
        df["Age"]=age
        print(df)
   ''' elif(a=="view spec"):
        roll1=[]
        roll=[]
        name=[]
        age=[]
        f=0
        cur.execute('select * from test')
        Roll_No=int(input('Roll NO: '))
        for i in cur:
            (a,b,c)=i
            roll1.append(a)
        for i in cur:
            (a,b,c)=i
            roll.append(a)
            name.append(b)
            age.append(c)
            if(a==Roll_No):
                break
        for m in roll1:
            f=m
            if(m==Roll_No):
                break  
        while(f!=Roll_No):
            print("Roll No NOT FOUND please RETRY")
            Roll_No=int(input('Roll NO: '))
        n="select * from test where Roll_No={}"
        n.format(Roll_No)
        cur.execute(n.format(Roll_No))
        df=py.DataFrame()
        df["Roll_No"]=roll
        df["Name"]=name
        df["Age"]=age
        print(df)
        #print("record deleted)")'''
    elif (a=="save"):
        roll=[]
        name=[]
        age=[]
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            roll.append(a)
            name.append(b)
            age.append(c)
        df=py.DataFrame()
        df["Roll_No"]=roll
        df["Name"]=name
        df["Age"]=age
        print(df)
        df.to_csv(r'C:\Users\athar\Desktop\CSV\Test.csv')
        print(r"Test.csv file is saved to the location-->'C:\Users\athar\Desktop\CSV\Test.csv'")
    elif(a=="delete"):
        roll=[]
        f=0
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            roll.append(a)
        
        Roll_No=int(input('Roll NO: '))
        for m in roll:
            f=m
            if(m==Roll_No):
                break  
        while(f!=Roll_No):
            print("Roll No NOT FOUND please RETRY")
            Roll_No=int(input('Roll NO: '))
        n="delete from test where Roll_No={}"
        n.format(Roll_No)
        cur.execute(n.format(Roll_No))
        print(Roll_No)
        print("record deleted")
    elif(a=="delete multiple"):
        n=int(input("No of records to be deleted"))
        roll=[]
        f=0
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            roll.append(a)
        for i in range(0,n,1):      
            Roll_No=int(input('Roll NO: '))
            for m in roll:
                f=m
                if(m==Roll_No):
                    break  
            while(f!=Roll_No):
                print("Roll No NOT FOUND please RETRY")
                Roll_No=int(input('Roll NO: '))
            n="delete from test where Roll_No={}"
            n.format(Roll_No)
            cur.execute(n.format(Roll_No))
            print(Roll_No)
            print("record deleted")
    elif(a=="delete all"):
        cur.execute("delete from test")
        print("Whole DATA Cleared")
    elif(a=="plot age"):
        print('EXIT graph to proceed')
        age=[]
        l=[]
        cur.execute('select * from test')
        for i in cur:
            (a,b,c)=i
            age.append(c)
        n=len(age)
        for i in range(1,n+1,1):
            l.append(i)
        pl.plot(l,age,marker='+')
        pl.show()
    elif(a=="exit"):
        asd=1
    else:
        print('WRONG COMMAND TRY AGAIN')
    con.commit()
