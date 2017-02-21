class Employee:
   raise_amount=1.04 # Class variables are same for every instance - has to access with 'class itself' or 'instance variables'.
   num_of_employees=0
   def __init__(self,first,last,pay):
       # pass # if you want to leave a class empty, you have to put pass
       self.first=first
       self.last=last # whereas instance variables are unique for each instance (emp_1, emp_2)
       self.pay=pay # instance variables access class attributes when class variables are defined, only if they don't have that attribute
       self.email = first + '.' + last + '@company.com'
       Employee.num_of_employees += 1
   def fullname(self):
       return '{} {}'.format(self.first, self.last)
   def apply_raise(self):
       self.pay = int(self.pay * self.raise_amount)
       return self.pay


print "No of employees at this moment: ", Employee.num_of_employees
emp_1=Employee('Sai Prasanna', 'Gundu', 50000)
print "Woah! no of employees: " ,Employee.num_of_employees
emp_2=Employee('Pravallika', 'Gundu', 600000)
print "No of employees now: ", Employee.num_of_employees

print "Full name of emp_1: ",(Employee.fullname(emp_1))
print "Full name of emp_2: ",(emp_2.fullname())

print "Email address of %r: "%(Employee.fullname(emp_1)),(emp_1.email)
print "Email address of %r:"%(emp_2.fullname()),(emp_2.email)

print (emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)

print "\nThere wouldn't be any raise amount attribute below for instance variable"
print "-"*50
print (emp_1.__dict__)

print "\nThere would be raise amount attribute which is a class variable"
print "-"*50
print (Employee.__dict__)

print "Defined class variable: ",(Employee.raise_amount) # using class variable directly
print "Instance variable emp_1: ",(emp_1.raise_amount) # using from class variable.

print "Let's play with variables."

emp_1.raise_amount=1.05
print "Setting instance variable emp_1.raise_amount to 1.05"
print "Instance variable emp_1: ",(emp_1.raise_amount)
print "Class variable Employee: ",(Employee.raise_amount)

Employee.raise_amount=1.06
print "Setting class variable Employee to 1.06"
print "Instance variable emp_2: ",(emp_2.raise_amount)
print "Class variable Employee: ",(Employee.raise_amount)

print "Total no. of employees: ", Employee.num_of_employees