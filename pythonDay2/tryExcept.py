'''
try:
    a=int(input("enter a number: "))
    b=int(input("enter a number2: "))    
    c=a/b
    print("Result: ",c)

except ZeroDivisionError:
    print("Check second number")
    
except IndexError:
    print("enter values")
    
except ValueError:
    print("Enter integer value")
'''

'''
try:
    a=int(input("enter a number: "))
    b=int(input("enter a number2: "))  
    if a<10:
        raise Exception
    else:
        print("ok")
    c=a/b
    print("Result: ",c)
    
except Exception as ex:
    print("The isuue is: ",ex)

finally:
    print("Ends here")
'''

'''
class MyException(Exception):
    def showMessage(self):
        print("My issue")
try:
    a=int(input("Enter the number: "))
    if a<10:
        raise MyException
    else:
        print("OK")
except MyException as ex:
    ex.showMessage()
'''

#---------assertion---------
a=int(input("Enter a number: "))
assert a<10, "Check this...."














