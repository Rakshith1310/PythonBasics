
import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv(r"C:\Users\User\Desktop\Materials\EmpData.csv")
#the above line is repeated many a times..:(
'''
dfg=df.groupby("City")
total=dfg["Payment"].sum()
total.plot(kind="bar")
'''
df=pd.read_csv(r"C:\Users\User\Desktop\Materials\StudentDataForPivot.csv")

'''
print(pd.pivot_table(df,index=['Name','Subject'],
                     values='Score',aggfunc="sum"))
'''

df=pd.read_csv(r"C:\Users\User\Desktop\Materials\EmpData.csv")
'''
plt.hist(df['Payment'],bins=5)
plt.show()
'''

df=pd.read_csv(r"C:\Users\User\Desktop\Materials\EmpData.csv")

'''
c=df.groupby(df['City'])
cp=['orange','magenta','blue']

c.sum().plot(kind='pie',y='Payment')
'''
'''

plt.scatter(df['Payment'],df['NoOfHours'],marker='o')
plt.show()
'''










