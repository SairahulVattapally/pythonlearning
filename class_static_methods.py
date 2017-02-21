class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay): # pass -- if you want to leave a class empty,                                            you have to put pass
        self.first=first
        self.last=last
        self.pay=pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps +=1
    def fullname(self):
       return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True

emp_1=Employee('Sai Prasanna', 'Gundu', 50000)
emp_2=Employee('Pravallika', 'Gundu', 600000)

emp_str_1= "SaiPrasanna-Gundu-70000"

Employee.set_raise_amount(1.05) # Class method calling

print (Employee.raise_amount)
print (emp_1.raise_amount)

new_emp_1=Employee.from_string(emp_str_1)
# calling the classmethod and the string of emp_str_1
# assign values to variable new_emp_1
print new_emp_1.email
print new_emp_1.fullname()


import datetime
my_date= datetime.date(2017, 2, 21)
print my_date
print "Working day: ",(Employee.is_workday(my_date))
