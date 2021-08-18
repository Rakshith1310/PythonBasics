'''
emp_name=input("Enter name: ")
city=input("Enter city")
emp_id=int(input("Enter emp no: "))
file_name=input("Enter file name: ")

obj=open(file_name,'a')
obj.write(emp_name+'\n')
obj.write(city+'\n')
obj.write(str(emp_id)+'\n\n')

print("data saved...")
obj.close()
'''

'''
x=input("enter file name to read: ")
f=open(x,'r')

str=f.read(2000) #characters to read
print(str)
f.close()
'''

'''
from datetime import datetime
time=datetime.now()

#transferring file on first day of every month
if time.day==1:
    x=input("enter file name to read: ")
    f=open(x,'r')
    str=f.read(2000)
    
    f2=open('newFile','w')
    f2.write(str)
    
    f2.close()
    f.close()
'''


'''
x=input("enter file name to read: ")
f=open(x,'r')

str=f.read(2000).split('\n')
def counting:
    uc,lc,dc=0,0,0
    for i in range(5):
        if str[i].isupper():
            uc=uc+1
        if str[i].islower():
            lc=lc+1
        if str[i].isdigit():
            dc=dc+1
        print("uppercase--",uc)
        print("lowercase--",lc)
        print("digits--",dc)
'''        

'''
f=open('empdata','r')
str=f.read(150)
print(str)

pos=f.tell() #current cursor location
print("Position--",pos,'\n')
pos=f.seek(2,0) #first parameter is wheretopointthe cursor
str=f.read(10)
print(str)
f.close()
'''

'''
f=open('empdata','r')
print(f.mode)
print(f.name)
print(f.closed)
'''

'''
import os
print(os.getcwd()) #prints current working directory
os.mkdir("newfolder11")
print("folder created")

os.rename("newfolder11","newfolder22")
print("folder successfully renamed")

os.rmdir("newfolder22")
print("folder deleted")

print(os.path.exists("newfolder22")) #returns false, bcaz just deleted

'''

import os
#print(os.name) #return nt in case of windows

#print(os.getcwd())
print(os.listdir("C:\\Users\\User\\Desktop\\FileHandling"))















































