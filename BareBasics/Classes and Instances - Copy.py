class Employee:
#__init__ is the constructor of an object
#when you create methods within a class, they receive the instance of the first class automatically, self
    raise_amount = 1.04
    num_of_emps = 0

#self = this from java
    def __init__(self, first, last, pay):
        self.first  = first
        self.last  = last
        self.pay  = pay
        self.email = first + '.' + last + '@hwemail.com'
        
        Employee.num_of_emps += 1 #in this case you don't want to use self because you don't want num_of_emps to be different for any particular instance

    def fullname (self):
        #the format function puts the objects from the parameters into their respective curly brackets
        print ('{} {}'.format (self.first, self.last))

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount would use the class amount not the instance

    @classmethod #@classmethod doesn't need a self
    def set_raise_amt (cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split ('-')
        return cls (first, last, pay) #creates the new employee

    @staticmethod #method should be a static if you don't access anything within a class or instance
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer (Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

#--------------------------------------------------------------------------------------------------------------------------------


emp_1 = Employee('Daniel', 'Hernandez', 500)
emp_2 = Employee('FakeDaniel', 'FakeHernandez', -500)

print (emp_1)
emp_1.apply_raise ()
print (emp_1)

Employee.raise_amount = 1.05 #changes it for the whole class
emp_1.apply_raise ()
print (emp_1)

Employee.set_raise_amt(10)
print (Employee.raise_amount)

emp_1.raise_amount = 2.0 #changes it for the instance

print (Employee.num_of_emps)

emp_str_3 = 'John-Doe-70000'
#first, last, pay = emp_str_3.split('-') if there wasn't an alternative contrucopr
emp_3 = Employee.from_string(emp_str_3)
print (emp_3.__dict__)

import datetime
my_date = datetime.date(2022, 7, 10)
print (my_date.weekday())
print (Employee.is_workday(my_date))

dev_1 = Developer('Dev', 'Master', 500, 'python')
print (dev_1.prog_lang)

#print (emp_1.email)
#print (emp_2.email)





#first plus last name, {} are placeholders
#print ('{} {}'.format (emp_1.first, emp_1.last))

#print (emp_1)
#print (emp_2)

#creates a instance variable called fist, last, email
#emp_1.first = 'Daniel'
#emp_1.last = 'Hernandez'
#emp_1.email = 'dhernandez1@hwemail.com'
#emp_1.pay = '100,000'

#emp_2.first = 'fakeDaniel'
#emp_2.last = 'fakeHernandez'
#emp_2.email = 'fakedhernandez1@hwemail.com'
#emp_2.pay = 'fake100,000'

#print (emp_1.email)
#print (emp_2.email)
