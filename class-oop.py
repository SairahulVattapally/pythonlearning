class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay): # pass # if you want to leave a class empty, you have to put pass
        self.first=first
        self.last=last
        self.pay=pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps +=1
    def fullname(self):
       return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
emp_1=Employee('Sai Prasanna', 'Gundu', 50000)
emp_2=Employee('Pravallika', 'Gundu', 600000)

print (Employee.fullname(emp_1))
print (emp_2.fullname())

print "Email address of %r: "%(Employee.fullname(emp_1)),(emp_1.email)
print "Email address of %r:"%(emp_2.fullname()),(emp_2.email)

