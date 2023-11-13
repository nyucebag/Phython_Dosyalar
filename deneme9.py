 
class Employee:
     
    num_of_emps = 0 
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
       # self.email=first+'.'+ last+'@company.com'
        Employee.num_of_emps += 1

    
         

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amount= amt

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True  


    def __repr__(self):
        return "Employee('{}, {},{} )".format(self.first, self.last, self.pay)



    def __str__(self):        
        return '{}, {}'.format(self.fullname(),self.pay)


    def __add__(self,other):
        return int(self.pay + other.pay)


    def __len__(self):
        return len(self.fullname())

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
            
    @property    
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)


    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if Employee is None:
            self.employees =[]
        else:    
            self.employees = employees  


    def add_emp(self,emp):
        if emp not in self.employees:
           self.employees.append(emp)       
           


    def remove_emp(self,emp):
        if emp in self.employees:
           self.employees.remove(emp)        
           



    def print_emps(self):
        for emp in self.employees:
            print('-->' ,emp.fullname)



    

emp_1=Employee('Nuray','Yucebag','50000')
emp_2=Employee('Nuray2','Yucebag2','60000')

# print(Employee.num_of_emps)


dev_1 = Developer('TestDeveloper','Test_Soyadi','120000','Python')
dev_2 = Developer('TestDeveloper2','Test_Soyadi2','150000','Java')


mgr_1 = Manager('MName1','MSurname1', 90000 ,[dev_1])

print(mgr_1.email)

print(mgr_1.print_emps())


# print(dev_1.email)

# print(dev_1.prog_lang)

#print(help(Developer))


# print(emp_1.first)    
# print(emp_2.email)


# print('{} {}'.format(emp_1.first, emp_2.first))

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))


# print(emp_1.raise_amount)
 
# print(emp_2.raise_amount)

# print(emp_1.__dict__)

# Employee.raise_amount=1.05


emp_1.set_raise_amt(1.06)

print(Employee.raise_amount)

print(emp_1.raise_amount)
 
print(emp_2.raise_amount)


emp_str_1 = 'Nuray-Yucebag-50000'
emp_str_2 = 'Nur-Hayat-20000' 
emp_str_3 = 'Ali-Alıhan-35000' 

first,last,pay = emp_str_1.split('-')

# new_emp_1 = Employee(first,last,pay)

new_emp_1=Employee.from_string(emp_str_1)


#print(new_emp_1.first +',' + new_emp_1.last +',' + new_emp_1.pay)


#import datetime
#mydate = datetime.date(2023,10,21)

#print(Employee.is_workday(mydate))

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.raise_amount)


# print(isinstance(mgr_1,Developer))

# print(issubclass(Manager,Employee))


# print(int.__add__(1,2))

# print(str.__add__('abc','2'))

# print(mgr_1.__repr__())

# print(emp_1+emp_2)

# print(len(emp_1))

# print(emp_1.email())


emp_1.fullname = 'Nurnuray Yucebag'
print(emp_1.first)
print(emp_1.last)

for emp in mgr_1.employees
    print(emp.email)
