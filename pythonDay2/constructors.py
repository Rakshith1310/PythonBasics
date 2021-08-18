'''
class Employee:
    emp_no=00
    name=''
    salary=0
    grade=''
    def get(self,id,name,salary):
        self.emp_no=id
        self.name=name
        self.salary=salary
    def check(self):
        if(self.salary)>30000:
            self.grade="A"
        else:
            self.grade="B"
    def show(self):
        self.check()
        print(self.emp_no)
        print(self.name)
        print(self.grade)
        print('nextEmp'.center(40,'-'))
 
        
 
empp=Employee()
empp.get(111,'messi',15000)
#empp.show()

emp2=Employee()
emp2.get(112,'kohli',34000)
#emp2.show()

#print(hasattr(emp2, 'emp_no'))
#print(getattr(emp2,'emp_no'))
setattr(emp2, 'salary', 45000)
#emp2.show()
#print(getattr(emp2,'salary'))
delattr(empp, 'salary')
delattr(empp, 'emp_no')
print(hasattr(empp, 'salary'))
print(hasattr(empp, 'emp_no'))
print(getattr(empp, 'salary'))
print(getattr(empp, 'emp_no'))
'''


#-----constructors------

class Employee:
    empno=0
    salary=0
    grade=''
    
    def __init__(self,empno,salary,grade):
        self.empno=empno
        self.salary=salary
        self.grade=grade
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
        
    def __del__(self):
        print('Destructor called')

emp=Employee(101, 45000, 'AA')
emp.show()
emp2=Employee(102, 42000, 'BB')
emp2.show()


















