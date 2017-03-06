class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@python.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1=Employee('Sai', 'Prasanna', 50000)
emp_2=Employee('Test','User', 70000)

print "Full name of emp_1:", emp_1.first + emp_1.last
# Using instance with methods
print emp_1.fullname()
print "email id of emp_1:",emp_1.email
# Using the class to call the variables and passing the instance emp_1
print Employee.fullname(emp_1)
