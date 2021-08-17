#formal p'arameters
'''def calc(a, b):
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
    
    
x=int(input("enter a number: "))
y=int(input("enter a number2: "))

#Actual parameters
calc(x,y)'''

'''def emp(id):
    d={'empId':id}
    print(d)
id=[101,102,122]
emp(id)'''

'''def show(emp_no, name, location):
    print('all here..',name, emp_no, location)

show(101,'abc','bengaluru')

print('next employee'.center(40,'*'))
show(name='xyz', location='mysuru',emp_no=102)
'''

'''def showData(*x):
    for i in x:
        print('value---',i)

showData(10,20)
showData('lool')
'''

'''def sum(*i):
    sum=0
    for x in i:
        sum=sum+x
    return sum

print(sum(10,20))'''

'''def some():
    global a
    print(a)
    a='hello'
    print(a)
a='My python'
some()'''
    
'''Hi = lambda x:x+5
print(Hi(12))'''
''''
def basicGenerator(x):
    for i in range(x):
        yield i

x=basicGenerator(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x)) #we face error here because forloop exceeds 5.
'''

x=[12,565,99,89,77,65,88,900,987]
y=[var for var in x if var%2!=0] #List of odd numbers

print(x)
print(y)

    
    
    
    
    
    















        
        
        
        