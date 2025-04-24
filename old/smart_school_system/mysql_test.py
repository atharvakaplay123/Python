import sys
#import getpass
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
asd="a"
print('WELCOME TO SMART STUDENT DATA MANAGEMENT SYSTEM')
print("Login to proceed")
u=input(str("UserID: "))
p=input(str("Password: "))
#p = getpass.getpass("Enter your password: ")
q=4
cur.execute('select * from login')
uid=[]
pas=[]
for i in cur:
    (a,b)=i
    uid.append(a)
    pas.append(b)
if (u in uid) and (p in pas) and (uid.index(u)==pas.index(p)):
    q=0
    if u=='admin':
        asd="b"
    else:
        asd="a"
while (u not in uid) or (p not in pas) or (q>1) or (uid.index(u)!=pas.index(p)):
    q=q-1
    print()
    print("Password you entered:", p)
    print("Incorrect login details please RETRY")
    print("NOTE: after 3 incorrect tries software will exit.")
    print("Attempts left",q)
    u=input(str("UserID: "))
    p=input(str("Password: "))
    #p = getpass.getpass("Enter your password: ")
    if u in uid and p in pas and uid.index(u)==pas.index(p):
        q=0
        if u=='admin':
            asd="b"
        else:
            asd="a"
if q==1:
    sys.exit("Too many incorrect attempts!!! Please Restart")

print()
print("Logged in as",u)
E=["mid_term", "annual", "class test", "Periodic1", "Periodic2"]
while(True):
    while(asd=="a"):
        print()
        F=py.read_csv('commands.csv')
        print('Enter the command to proceed.')
        print(F)
        a=str(input('Enter command:'))
        if (a=="insert marks"):
            roll=[]
            cur.execute('select * from test')
            for i in cur:
                (a,b,c)=i
                roll.append(a)
            Roll_No=int(input('Roll NO: '))
            while(Roll_No<1000 or Roll_No>10000):
                print("Roll No should be 4 digit")
                Roll_No=int(input('Roll NO: '))
                while Roll_No not in roll:
                    print("Roll No not found in student data, please try again")
                    Roll_No=int(input('Roll NO: '))
            while Roll_No not in roll:
                print("Roll No not found in student data, please try again")
                Roll_No=int(input('Roll NO: '))
                while(Roll_No<1000 or Roll_No>10000):
                    print("Roll No should be 4 digit")
                    Roll_No=int(input('Roll NO: '))
            phy=int(input('Physics: '))
            chem=int(input('Chemistry: '))
            maths=int(input('Maths: '))
            eng=int(input('English: '))
            ip=int(input('IP: '))
            print("Select exam from the list", E)
            exam=str(input('Exam: '))
            while exam not in E:
                print("plese select from the given list",E)
                exam=str(input('Exam: '))
            query=('insert into marksheet(Roll_No,physics,chemistry,mathematics,english,ip,exam)''values(%s,%s,%s,%s,%s,%s,%s)')
            values=(Roll_No,phy,chem,maths,eng,ip,exam)
            cur.execute(query,values)
            print('SAVED TO MARKSHEET')
        elif (a=="insert marks multiple"):
            print("Select exam from the list", E)
            exam=str(input("exam: "))
            while exam not in E:
                print("please select exam from the list", E)
                exam=str(input("exam: "))
            n=int(input("no of entries to insert"))
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
                    while Roll_No not in roll:
                        print("Roll No not found in student data, please try again")
                        Roll_No=int(input('Roll NO: '))
                while Roll_No not in roll:
                    print("Roll No not found in student data, please try again")
                    Roll_No=int(input('Roll NO: '))
                    while(Roll_No<1000 or Roll_No>10000):
                        print("Roll No should be 4 digit")
                        Roll_No=int(input('Roll NO: '))
                phy=int(input('Physics: '))
                chem=int(input('Chemistry: '))
                maths=int(input('Maths: '))
                eng=int(input('English: '))
                ip=int(input('IP: '))
                query=('insert into marksheet(Roll_No,physics,chemistry,mathematics,english,ip,exam)''values(%s,%s,%s,%s,%s,%s,%s)')
                values=(Roll_No,phy,chem,maths,eng,ip,exam)
                cur.execute(query,values)
                print('SAVED TO MARKSHEET')
        elif (a=="import student scorecard"):
            n=str(input("Location: "))
            df=py.read_csv(n)
            while df.shape!=(5,8):
                print("invalid formate please try another file")
                print(df.shape)
                n=str(input("Location: "))
                df=py.read_csv(n)
                if df.shape==(5,8):
                    break
            if df.shape==(5,8):
                print(df)
                l2=list(df["percentage"])
                l1=list(range(1,len(l2)+1))
                pl.plot(l1,l2)
                print("Exit graph to continue")
                pl.show()
                print("We are working on this feature, so only the graph will be shown and imported data is not stored in database")
        elif (a=="insert"):
            roll=[]
            cur.execute('select * from test')
            for i in cur:
                (a,b,c)=i
                roll.append(a)
            Roll_No=int(input('Roll NO: '))
            while(Roll_No<1000 or Roll_No>10000):
                print("Roll No should be 4 digit")
                Roll_No=int(input('Roll NO: '))
                while Roll_No in roll:
                    print("Roll No Repeted, Please try again")
                    Roll_No=int(input('Roll NO: '))
            while Roll_No in roll:
                print("Roll No Repeted, Please try again")
                Roll_No=int(input('Roll NO: '))
                while(Roll_No<1000 or Roll_No>10000):
                    print("Roll No should be 4 digit")
                    Roll_No=int(input('Roll NO: '))
            Name=str(input('Name: '))
            Age=int(input('Age: '))
            query=('insert into test(Roll_No,Name,Age)''values(%s,%s,%s)')
            values=(Roll_No,Name,Age)
            cur.execute(query,values)
            print('SAVED TO DATABASE')
        elif (a=="insert multiple"):
            n=int(input("no of entries to insert"))
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
                    while Roll_No in roll:
                        print("Roll No Repeted, Please try again")
                        Roll_No=int(input('Roll NO: '))
                while Roll_No in roll:
                    print("Roll No Repeted, Please try again")
                    Roll_No=int(input('Roll NO: '))
                    while(Roll_No<1000 or Roll_No>10000):
                        print("Roll No should be 4 digit")
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
            print("Type 'export' to export this data or press enter to go to main menu")
            al=str(input("Command: "))
            if al=="export":
                j=r'Data.csv'
                df.to_csv(j)
                print(r"Test.csv file is saved to the location-->",j)
        elif (a=="view marksheet"):
            print()
            print("select exam from the list", E)
            exam=str(input("exam: "))
            while exam not in E:
                print("please select exam from the list", E)
                exam=str(input("exam: "))
            roll=[]
            phy=[]
            chem=[]
            mat=[]
            ip=[]
            eng=[]
            d='"'+exam+'"'
            n="select * from marksheet where exam="+d 
            cur.execute(n)
            for i in cur:
                (a,b,c,d,e,f,g)=i
                roll.append(a)
                phy.append(b)
                chem.append(c)
                mat.append(d)
                eng.append(e)
                ip.append(f)
            o={a:roll,b:phy,c:chem,d:mat,}
            df=py.DataFrame()
            df["Roll_No"]=roll
            df["Physics"]=phy
            df["Chemistry"]=chem
            df["Maths"]=mat
            df["English"]=eng
            df["ip"]=ip
            print(df)
            print("Type 'export' to export this data or press enter to go to main menu")
            al=str(input("Command: "))
            if al=="export":
                j=r'marksheet_' + exam + r'.csv'
                df.to_csv(j)
                print(r"Test.csv file is saved to the location-->",j)
            elif al=="plot":
                k=str(input("subject"))
                print('EXIT graph to proceed')
                l=[]
                n=len(phy)
                for i in range(1,n+1,1):
                    l.append(i)
                pl.plot(l,phy,marker='+')
                pl.show()
        elif (a=="view student scorecard"):
            print()
            r=[]
            roll=[]
            phy=[]
            chem=[]
            mat=[]
            ip=[]
            eng=[]
            exam=[]
            total=[]
            per=[]
            Name=""
            cur.execute("select Roll_No from marksheet")
            for i in cur:
                (a,)=i
                if a not in r:
                    r.append(a)
            Roll_No=int(input("Enter Roll NO: "))
            while Roll_No not in r:
                print("Roll No NOT FOUND please RETRY")
                Roll_No=int(input('Enter Roll NO: '))
            n="select * from test where Roll_No={}"
            n.format(Roll_No)
            cur.execute(n.format(Roll_No))
            for i in cur:
                (a,b,c)=i
                Name=b
            n="select *,physics+chemistry+mathematics+english+ip,(physics+chemistry+mathematics+english+ip)/5 from marksheet where Roll_No={}"
            n.format(Roll_No)
            cur.execute(n.format(Roll_No))
            print("Roll No: ",Roll_No)
            print("Name: ",Name)
            for i in cur:
                (a,b,c,d,e,f,g,h,j)=i
                roll.append(a)
                phy.append(b)
                chem.append(c)
                mat.append(d)
                eng.append(e)
                ip.append(f)
                exam.append(g)
                total.append(h)
                per.append(j)
            df=py.DataFrame()
            df["Physics"]=phy
            df["Chemistry"]=chem
            df["Maths"]=mat
            df["English"]=eng
            df["ip"]=ip
            df["exam"]=exam
            df["total"]=total
            df["percentage"]=per

            print(df)
            print("Type 'export' to export this data or Type 'plot' to plot student graph or press enter to go to main menu")
            al=str(input("Command: "))
            if al=="export":
                j=r'scorecard_' + str(Roll_No) + r'.csv'
                df.to_csv(j)
                print(r"Test.csv file is saved to the location-->",j)
            elif al=="plot":
                print('EXIT graph to proceed')
                l=[]
                n=len(phy)
                for i in range(1,n+1,1):
                    l.append(i)
                pl.plot(l,per,marker='+')
                pl.title("Graph of student [Roll No: "+str(Roll_No)+" Name: "+Name+"]")
                pl.xlabel("Exams given by student-->")
                pl.ylabel("Percentage of student-->")
                pl.grid()
                k=[1,2,3,4,5]
                pl.xticks(k,exam)
                pl.show()
        elif (a=="view spec"):
            roll1=[]
            roll=[]
            name=[]
            age=[]
            cur.execute('select * from test')
            for i in cur:
                (a,b,c)=i
                roll.append(a)
            Roll_No=int(input('Roll NO: '))
            while Roll_No not in roll:
                print("Roll No NOT FOUND please RETRY")
                Roll_No=int(input('Roll NO: '))
            n="select * from test where Roll_No={}"
            n.format(Roll_No)
            cur.execute(n.format(Roll_No))
            for i in cur:
                (a,b,c)=i
                roll1.append(a)
                name.append(b)
                age.append(c)
            df=py.DataFrame()
            df["Roll_No"]=roll1
            df["Name"]=name
            df["Age"]=age
            print(df)
        elif (a=="delete"):
            roll=[]
            cur.execute('select * from test')
            for i in cur:
                (a,b,c)=i
                roll.append(a)       
            Roll_No=int(input('Roll NO: '))  
            while Roll_No not in roll:
                print("Roll No NOT FOUND please RETRY")
                Roll_No=int(input('Roll NO: '))
            print("Note: Deleting this will also remove students' marks. Are you sure you want to proceed? if yes type'yes',or press enter to go back")
            p=str(input("Command: "))
            if p=="yes":
                n="delete from marksheet where Roll_No={}"
                n.format(Roll_No)
                cur.execute(n.format(Roll_No))          
                n="delete from test where Roll_No={}"
                n.format(Roll_No)
                cur.execute(n.format(Roll_No))
                print(Roll_No)
                print("Record Deleted")
        elif (a=="delete multiple"):
            N=int(input("No of records to be deleted: "))
            for i in range(0,N,1):
                roll=[]
                cur.execute('select * from test')
                for i in cur:
                    (a,b,c)=i
                    roll.append(a)       
                Roll_No=int(input('Roll NO: '))  
                while Roll_No not in roll:
                    print("Roll No NOT FOUND please RETRY")
                    Roll_No=int(input('Roll NO: '))
                print("Note: Deleting this will also remove students' marks. Are you sure you want to proceed? if yes type'yes',or press enter to go back")
                p=str(input("Command: "))
                if p=="yes":
                    n="delete from marksheet where Roll_No={}"
                    n.format(Roll_No)
                    cur.execute(n.format(Roll_No))          
                    n="delete from test where Roll_No={}"
                    n.format(Roll_No)
                    cur.execute(n.format(Roll_No))
                    print(Roll_No)
                    print("Record Deleted")
                else:
                    break
        elif (a=="clear markslist"):
            cur.execute("delete from marksheet")
            print("Whole DATA Cleared")
        elif (a=="clear"):
            cur.execute("delete from marksheet")
            cur.execute("delete from test")
            print("Whole DATA Cleared")
        elif (a=="exit"):
            sys.exit("exit")
        elif (a=="logout"):
            asd="c"
            print()
            print('WELCOME TO SMART STUDENT DATA MANAGEMENT SYSTEM')
            print("Login to proceed")
            u=input(str("UserID: "))
            p=input(str("Password: "))
            q=4
            cur.execute('select * from login')
            uid=[]
            pas=[]
            for i in cur:
                (a,b)=i
                uid.append(a)
                pas.append(b)
            if (u in uid) and (p in pas) and (uid.index(u)==pas.index(p)):
                q=0
                if u=='admin':
                    asd="b"
                    print(asd)
                    break
                else:
                    asd="a"
                    break
            while (u not in uid) or (p not in pas) or (q>1) or (uid.index(u)!=pas.index(p)):
                q=q-1
                print()
                print("Password you entered:", p)
                print("Incorrect login details please RETRY")
                print("NOTE: after 3 incorrect tries software will exit.")
                print("Attempts left",q)
                u=input(str("UserID: "))
                p=input(str("Password: "))
                #p = getpass.getpass("Enter your password: ")
                if u in uid and p in pas and uid.index(u)==pas.index(p):
                    q=0
                    if u=='admin':
                        asd="b"
                        break
                    else:
                        asd="a"
                        break
            if q==1:
                sys.exit("Too many incorrect attempts!!! Please Restart")

            asd="a"
        else:
            print('WRONG COMMAND TRY AGAIN')
        con.commit()
    while(asd=="b"):
        print()
        print("This is Admin Consol")
        F=py.read_csv('commands_admin.csv')
        print('Enter the command to proceed.')
        print(F)
        a=str(input('Enter command:'))
        if (a=="view passwords"):
            df=py.DataFrame()
            cur.execute('select * from login')
            uid=[]
            pas=[]
            for i in cur:
                (a,b)=i
                uid.append(a)
                pas.append(b)
            df["UID"]=uid
            df["Password"]=pas
            print(df)
        elif (a=="add account"):
            h=str(input("Enter UID for new account: "))
            j=str(input("Enter Password for new account: "))
            k=str(input("Confirm Password: "))
            uid=[]
            pas=[]
            cur.execute('select * from login')
            for i in cur:
                (a,b)=i
                uid.append(a)
                pas.append(b)
            while h in uid:
                print("UID already exists, try again with another UID")
                h=str(input("Enter UID for new account: "))
                j=str(input("Enter Password for new account: "))
            while j!=k:
                print("The passwords you entered are different. Please re-enter your password.")
                j=str(input("Enter Password for new account: "))
                k=str(input("Confirm Password: "))
            if h not in uid and j==k:
                query=('insert into login(UIDs,passwords)''values(%s,%s)')
                values=(h,j)
                cur.execute(query,values)
                print('New Account Created')
        elif (a=="remove account"):
            h=str(input("Enter UID to remove account: "))
            j=str(input("Enter Password: "))
            uid=[]
            pas=[]
            cur.execute('select * from login')
            for i in cur:
                (a,b)=i
                uid.append(a)
                pas.append(b)
            while h not in uid or j not in pas or uid.index(h)!=pas.index(j):
                print("Details you entered are wrong, try again")
                h=str(input("Enter UID for new account: "))
                j=str(input("Enter Password for new account: "))
            while h=="admin":
                print("You will need administrator's permission to do this.\nContact Administrator\nTry Again")
                h=str(input("Enter UID to remove account: "))
                j=str(input("Enter Password: "))            
            if h in uid and j in pas and uid.index(h)==pas.index(j) and h!="admin":
                query='delete from login where UIDs='+"'"+h+"'"
                #print(query)
                cur.execute(query)
                print("[user: "+h+"],  [Password: " +j+"]")
                print('Account Removed')
        elif (a=="logout"):
            asd="c"
            print()
            print('WELCOME TO SMART STUDENT DATA MANAGEMENT SYSTEM')
            print("Login to proceed")
            u=input(str("UserID: "))
            p=input(str("Password: "))
            q=4
            cur.execute('select * from login')
            uid=[]
            pas=[]
            for i in cur:
                (a,b)=i
                uid.append(a)
                pas.append(b)
            if (u in uid) and (p in pas) and (uid.index(u)==pas.index(p)):
                q=0
                if u=='admin':
                    asd="b"
                    break
                else:
                    asd="a"
                    break
            while (u not in uid) or (p not in pas) or (q>1) or (uid.index(u)!=pas.index(p)):
                q=q-1
                print()
                print("Password you entered:", p)
                print("Incorrect login details please RETRY")
                print("NOTE: after 3 incorrect tries software will exit.")
                print("Attempts left",q)
                u=input(str("UserID: "))
                p=input(str("Password: "))
                #p = getpass.getpass("Enter your password: ")
                if u in uid and p in pas and uid.index(u)==pas.index(p):
                    q=0
                    if u=='admin':
                        asd="b"
                        break
                    else:
                        asd="a"
                        break
            if q==1:
                sys.exit("Too many incorrect attempts!!! Please Restart")

            asd="a"
        elif (a=="exit"):
            sys.exit("exit")
        else:
            print('WRONG COMMAND TRY AGAIN')
        con.commit()