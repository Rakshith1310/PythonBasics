import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
x=[10,20,30]
y=[100,44,99]

x1=[99,65,22]
y1=[33,21,43]

plt.plot(x,y,'--g') #==g represents color of the plot
plt.plot(x1,y1,'--r')
plt.show()
'''

'''
sem=[1,2,3]

student1=[66,77,88]
student2=[52,48,76]

plt.plot(sem,student1,label='kamala')
plt.plot(sem,student2,label='joe')
plt.legend()

plt.xlabel('Semesters')
plt.ylabel("Marks")
plt.show()
'''

'''
sem=[1,2,3]

student1=[66,77,88]
plt.bar(sem,student1)
plt.title('Bar graph')
plt.show()
'''

'''
oddsem=[1,3,5]
evensem=[2,4,6]

oddmarks=[66,77,88]
evenmarks=[52,48,76]

plt.bar(oddsem,oddmarks, color='r')
plt.bar(evensem,evenmarks, color='b')
plt.show()
'''

'''
empdict={'rollo':[100,101,102],
   'name':['Joe','kamala','messi'],
   'salary':[99000,85000,75000]}
df=pd.DataFrame(empdict)
df['tax']=df['salary']*(.30)

print(df)
plt.bar(df.salary,df.tax)
plt.legend()
plt.xlabel('salary')
plt.ylabel('tax')
'''

'''
ct=['India','US','UK']
pop=[1.35,1.80,1]

y=np.arange(len(ct))
plt.bar(y,pop)
plt.xticks(y,ct)
plt.show()


ct=['India','US','UK']
pop=[1.35,1.80,1]

y=np.arange(len(ct))
plt.barh(y,pop)
plt.xticks(y,ct)
plt.show()
'''

'''
x=[10,20,30]
y=[100,44,99]

plt.scatter(x,y)
plt.show()
'''

'''
ages=[12,13,15,11,12,15,33,35,37,33,32,31,55,54,56,59,51,10]
plt.hist(ages, bins=3)
plt.show()
'''

'''
label=['karnataka','ap','tn','delhi']
lits=[125,100,45,65]
color=['grees','red','yellow','blue']
e=[0.1,0,0,0]

plt.pie(lits,explode=e,labels=label)
plt.show()
'''
'''
dicti={'unemployement':[4.5,3.4,7.8,6.7,9.9],
       'marketshare':[1200,1350,1400,1990,1670]}

df=pd.DataFrame(dicti, columns=['unemployement','marketshare'])
print(df)

df.plot(x='unemployement',
        y='marketshare',kind='scatter')
'''

'''
d={'year':[1971,1977,1983,1989,1995],
   'population':[5,5.5,6,5.4,6]}
df=pd.DataFrame(d)

df.plot(x='year',y='population', kind='line')


d={'country':['India','UK','US'],
   'gdp':[5,9,8]}

df=pd.DataFrame(d)
df.plot(x='country',y='gdp', kind='bar')
'''

import pymysql
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',
                  db='fis')
cur=d.cursor()
sql='select * from employee'
cur.execute(sql)
df=cur.fetchall()

df=pd.DataFrame(df, columns=['empid','name','city','salary'])


df.plot(x='name',y='salary',kind='bar')

















