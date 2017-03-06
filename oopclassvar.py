class Employee:
    raise_amount= 1.04
    num_of_emps=0
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@python.com'
        Employee.num_of_emps +=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        # type: () -> object
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

print (Employee.num_of_emps)
emp_1=Employee('Sai', 'Prasanna', 50000)
emp_2=Employee('Test', 'User', 60000)

# print emp_1.fullname()
# print Employee.fullname(emp_2)
emp_1.raise_amount=1.06
print (Employee.num_of_emps)
print (emp_1.__dict__)
print (emp_1.raise_amount)
print (Employee.raise_amount)
print (emp_2.raise_amount)
print (Employee.num_of_emps)

#print emp_1.pay
#print emp_1.apply_raise()