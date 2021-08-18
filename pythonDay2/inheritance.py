'''
class A:
    def hello(self):
        print("Hello from parent")
        
class B(A):
    def sum(self,a,b):
        print('Sum: ',(a+b))
        
class C(B):
    def multiply(self,a,b):
        print('Product: ',(a*b))
        
class D(B,A): #here order of a,b is vital
    def greet(self):
        print('This is DD')

obj=B()
obj.hello()
obj.sum(12, 10)

obj1=C()
obj1.hello()
obj1.sum(12, 10)
obj1.multiply(10, 10)

obj2=D()
obj2.greet()
obj2.hello()
'''

class A:
    __name='Rakshith' #This is hidden
    def hello():
        print('hello!')
    def __str__(self):
        return "This is an object"
obj=A()
print(obj)
print(obj.__name) #gives error, because hidden


