import pandas as pd
data={'Name':['abc','bca','cba'],
      'class':['XII','XII','XI'],
      'Section':['A','A','A']}
data1=[
    {'Name':'abc'},
    {'class':'XII'},
    {'Section':'A'}]
data2=[
    {'Name':'bca'},
    {'class':'XII'},
    {'Section':'A'}]
l=[data1,data2]
df1=pd.DataFrame(data)
df=pd.read_csv(r'C:\Users\athar\Desktop\Book1.csv')#reading from csv
df2=pd.DataFrame(index=['A','B','C','D'])
df2['COL1']=[1,2,3,4]
df2['COL2']=[2,3,4,5]
df2['COL3']=[3,4,5,6]
df2['COL4']=[4,5,6,7]
df['abc']=[1,2,3]#adding new column
df2.loc['E',:]=[32,23,45,65]#adding new row
df2.COL4['E']=37#modifing a single cell
print("NOT Transposed")
print(df2)
print()
print("Transposed")
print(df2.T)#transposed
print(df2.drop(['B']))#deleting a row
del df2['COL4']#deleting a column
print()
print(df2)
a=df2.loc[:,["COL2","COL3"]]
print(a)
