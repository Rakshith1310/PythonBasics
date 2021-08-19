import pandas as pd


df=pd.read_csv(r"C:\Users\User\Desktop\Materials\salaries.csv")
#print(df)

'''
print(df.head(3))
print(df.tail(2))

print(df.dtypes)
print(df.shape)
'''

#print(df[3:])   #3rd row onwards
#print(df[:3]) #till 2nd rowx


#print(df.iloc[0:2,0:3]) #first two rows and first three columns

#conditional data
#print(df[(df['salary']>90000)&
#         (df['discipline']=='B')])


'''
df.insert(6,'test',df['service']+20) #6 specifies the column number..
print(df)
'''

#'''
#df=pd.read_csv(r"C:\Users\User\Desktop\Materials\salaries.csv")
#df1=pd.read_csv(r"C:\Users\User\Desktop\Materials\salaries1.csv")

#df2=df.append(df1)
#print(df2.head(7))


#'''
#df=pd.read_csv(r"C:\Users\User\Desktop\Materials\salaries.csv")

#print(df.sort_values('salary',ascending=False))
#print('descending over, now ascending'.center(68),'-')
#print(df.sort_values('salary',ascending=True))
#'''

df=pd.read_csv(r"C:\Users\User\Desktop\Materials\salaries.csv")





















