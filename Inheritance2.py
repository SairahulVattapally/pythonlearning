class  Employee:
    raise_amt= 1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@python.com'
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)
        return self.pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay, prog_lang):
        Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang

#print (help(Developer))
#print dev1.email
#print dev1.apply_raise()
#print dev2.apply_raise()

class Manager(Employee):
    def __init__(self,first,last,pay, employee=None):
        Employee.__init__(self,first,last,pay)
        if employee is None:
            self.employee = []
        else:
            self.employee=employee
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    def remv_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
    def all_emp(self):
        for emp in self.employee:
            print '->', emp.fullname()

dev1=Developer('Sai','Prasanna', 70000,'Python')
dev2=Developer('Pratyusha','Sargam', 60000,'Java')
mgr_1=Manager('Chandu','Reddy',80000,[dev1])

#print (help(Manager))

print mgr_1.email
print mgr_1.fullname()
mgr_1.remv_emp(dev1)
mgr_1.add_emp(dev1)
mgr_1.add_emp(dev2)
print mgr_1.all_emp()
print dev2.prog_lang

print isinstance(mgr_1,Developer)
print issubclass(Manager,Developer)