'''
import pymysql

d=pymysql.connect(host='localhost',
                user='root',
                password='Cloud@123$',
                db='fis')

cur=d.cursor()

sql="select * from employee"

cur.execute(sql)
data=cur.fetchall()
for res in data:
    print('EmpNo--',res[0])
    print('Name--',res[1])
    print('City--',res[2])
    print('Salary--',res[3])
d.close()
'''

'''
try:
    sql="insert into employee values(104,'Messi','madrid',55000)"
    cur.execute(sql)
    print("Inserted")
    d.commit()

except Exception as ex:
    print(ex)

d.close()
'''

'''
try:
    sql="delete from employee where empno=104"
    cur.execute(sql)
    print("Deleted")
    d.commit()

except Exception as ex:
    print(ex)

d.close()
'''

'''
try:
    sql="select * from employee"
    cur.execute(sql)
    data=cur.fetchall()
    print("------Data--------")
    for res in data:
        print("-----------------")
        print('EmpNo--',res[0])
        print('Name--',res[1])
        print('City--',res[2])
        print('Salary--',res[3])
        
except Exception as ex:
    print(ex)

d.close()
'''

'''
try:
    sql="update employee set salary=85000 where empno=100"
    cur.execute(sql)
    print("record executed")
    d.commit()
except Exception as ex:
    print(ex)
d.close()
'''

'''
import pymysql

d=pymysql.connect(host='localhost',
                user='root',
                password='Cloud@123$',
                db='fis')

cur=d.cursor()
try:
    empno=int(input("Enter empno: "))
    ename=input("Enter name: ")
    city=input("Enter city: ")
    salary=int(input("Enter salary: "))
    
    sql="insert into employee values(%d,'%s','%s',%d)"%(empno,ename,city,salary)
    cur.execute(sql)
    print("record saved")
    d.commit()
except Exception as ex:
    print(ex)
d.close()
'''

'''
import pymysql
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
cursor=d.cursor()

try:
    eno=int(input("Enter eno to fetch details: "))
    sql="select * from employee where empno=%d"%(eno)
    cursor.execute(sql)
    data=cursor.fetchone()
    if(data):
        print("---------data found--------")
        print(data)
    else:
        print("-----Data not found------\nEnter details to add")
        empno=int(input("Enter empno: "))
        ename=input("Enter name: ")
        city=input("Enter city: ")
        salary=int(input("Enter salary: "))
        
        sql="insert into employee values(%d,'%s','%s',%d)"%(empno,ename,city,salary)
        cursor.execute(sql)
        print("-----Record saved----------")
        d.commit()
except Exception as ex:
    print(ex)
d.close()
'''














