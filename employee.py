


class Employee:
    
    def __int__ (self, fname, lname, pay):
        self.fname= fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

#emp_1 = Employee('Corey', 'Martin', 50000)
emp_2 = Employee('James', 'Mwiti', 60000)

print(emp_2.email)