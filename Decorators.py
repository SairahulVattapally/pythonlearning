class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return '{}.{}@python.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print ('Delete Name!')
        self.first=None
        self.last=None
        return

emp_1=Employee('Sai', 'Prasanna', 500000)
emp_1.fullname = 'Sai Baba'
emp_1.first='Rahul'

print (emp_1.fullname)
print (emp_1.email)
print (emp_1.first)

del emp_1.fullname
