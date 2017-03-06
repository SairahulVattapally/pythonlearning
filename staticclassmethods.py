class Employee:
    raise_amt=1.05
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@python.com'
        Employee.num_of_emps +=1
    # We pass self for regular methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amt)
    @classmethod
    # We pass cls for class methods
    def set_raise_amt(cls, amount):
        cls.raise_amt=amount
        return cls.raise_amt
    @classmethod
    def from_string(cls,empstr):
        first,last, pay = empstr.split('-')
        return cls(first,last,pay)
    @staticmethod
    # We pass manual arg for static methods
    def isworkday(day):
        if day.weekday == 5 or day.weekday ==6:
            return False
        return True

emp_1=Employee('Sai','Prasanna',80000)
emp_2=Employee('Test','User',90000)

empstr_1 = 'John-Mason-80000'
empstr_2= 'Sai-Prasanna-70000'

# Using class methods as alternative constructors
newemp_1=Employee.from_string(empstr_1)
newemp_2=Employee.from_string(empstr_2)

print newemp_1.email
print newemp_2.email
#emp_1.set_raise_amt(1.12)
#print emp_1.raise_amt
#print Employee.set_raise_amt(1.13)
#print emp_1.raise_amt

import datetime
print "Veryfing the day is holiday or working day...\n"
year=raw_input("Enter the current year:")
x=int(year)
month=raw_input("Enter the month of this year:")
y=int(month)
day=raw_input("Enter the day of this year:")
z=int(day)
my_date=datetime.date(x,y,z)
# Calling the function & passing the values to static method
print "Is it working day?", Employee.isworkday(my_date)