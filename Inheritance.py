# Inheritance Example
class Employee:
    raise_amt=1.05
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email = first +'.'+last+ '@python.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang): # Inherits from parent & current class
        #super().__init__(first,last,pay)
        Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang


dev1=Developer("Sai","Prasanna",70000,'Python')
dev2=Developer("Test","User",80000,'Java')


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees=employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def all_emp(self):
        for emp in self.employees:
            print ("->", emp.fullname())

mgr_1=Manager('Sai','Pratyusha',80000,[dev1])

print mgr_1.email
print mgr_1.fullname()
print "Adding employee 2.."
print mgr_1.add_emp(dev2)
print mgr_1.all_emp()

print "Removing the employee 1.."
mgr_1.remove_emp(dev1)
print mgr_1.all_emp()

print "Again adding the employee 1.."
mgr_1.add_emp(dev1)
print mgr_1.all_emp()

print isinstance(mgr_1,Manager)
print isinstance(dev1,Employee)
print isinstance(dev1,Manager)
print issubclass(Developer,Employee)
print issubclass(Manager,Developer)
#print dev1.email
#print dev1.prog_lang

# Takes the variable i.e raise_amt from Employee
#print "\nIntial pay of dev1:", dev1.pay
#dev1.apply_raise()
#print "Final pay of dev1 after raise for 5% increase:",dev1.pay

# Takes the variable i.e raise_amt from Developer
#print "\nIntial pay of dev2:", dev2.pay
#dev2.apply_raise()
#print "Final pay of dev1 after raise 10% increase:",dev2.pay

#print dev2.pay
# print (help(Developer))