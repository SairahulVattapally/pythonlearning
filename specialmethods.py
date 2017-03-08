class Employee:
    raise_amt=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first +'.'+ last + '@python.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)

    def __str__(self):
        return '{}-{}'.format(self.email, self.fullname())

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1=Employee('Sai','Prasanna', 500000)
emp_2=Employee('Pratyusha','Sargam', 600000)

#print len(emp_1.fullname())
#print emp_1.fullname().__len__()
print len(emp_1)

print (emp_1+emp_2)

#print int.__add__(1,2)
#print str.__add__('Sai',' Prasanna')

#print(emp_1)
#print repr(emp_1)
#print str(emp_1)

#str(emp_1)
#print emp_1.__str__()
#print emp_1.__repr__()
