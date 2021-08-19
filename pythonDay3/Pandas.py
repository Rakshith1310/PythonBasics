import pandas as pd
#s=pd.Series()
#print(s)

'''
s=pd.Series([35,45,55,65], index=[90,99,88,77]) #assigns index value as well
print(s)



s=pd.Series([35,45,55,65], index=['p','q','r','s'])
print(s['s'])

d={'Rollno':101,'name':'Rakshith','city':'Bengaluru'}
s=pd.Series(d)  #dictionary as series...
print(s)

s=pd.Series(d,index=['city','Rollno','name'])   #specifying indices
print(s)

s=pd.DataFrame(8,index=['p','q','r','s'])
print(s)
'''

'''
d={'rollo':[100,101,102],
   'name':['Joe','kamala','messi'],
   'city':['manahatten','florida','mandya']}
df=pd.DataFrame(d, index=['rank1','rank2','rank3'])
df['newroll']=df['rollno']+10
print(df)
'''

empdict={'rollo':[100,101,102],
   'name':['Joe','kamala','messi'],
   'salary':[99000,85000,75000]}
df=pd.DataFrame(empdict)

df['hra']=df['salary']*(0.12)
df['totalSalary']=df['hra']+df['salary']

print(df)






