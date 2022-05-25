import re;
from DB_Handler import DBConnection
class Person(object):
    __healthRate=0;
    def __init__(self, full_name,money,sleepmood,healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.setHealthRate(healthRate)
    
    def sleep(self):
        print("sleeping")
        
    def eat(self):
        print("eating")

    def buy(self):
        print("buying")
    def setHealthRate(self,healthRateInput):
        if(healthRateInput>0 and healthRateInput <=100):
            self.healthRate=healthRateInput;
        else:
            print("health must be between 100 and 0 ")


class Employee(Person):
    def __init__(self,full_name,money,sleepmood,healthRate,workmood,is_manager,email,salary):
       super().__init__(full_name,money,sleepmood,healthRate)
    #    self.id = id
       self.setEmail(email)
       self.workmood = workmood
       self.setSalary(salary)
       self.is_manager = is_manager
    
    def setEmail(self,emailInput):
        isValid=re.search("^[a-z]*@[a-z]*.com$",emailInput)
        if(isValid):
            self.email=emailInput;
        else:
            print("email format is not valid")

    def setSalary(self,salaryInput):
        if(salaryInput>=1000):
            self.salary = salaryInput;
        else:
            print("salary should be between 0 and 1000")

    
    def sleep(self,hours):
        if(hours==7):
            print("happy")
        elif(hours>7):
            print("lazy")
        elif(hours<7):
            print("tired")
        
    def eat(self,meals):
        if(meals==3):
            self.setHealthRate(100)
        elif(meals>2):
            self.setHealthRate(75)
        elif(meals<1):
            self.setHealthRate(50)
    def buy(self,items):
        self.money-=(items*10)

    
    def work(self,hours):
         if(hours==8):
                print("happy")
         elif(hours>8):
            print("lazy")
         elif(hours<8):
            print("tired")
    def sendEmail(self,to,subject,bodyreceiver_name):
        f = open('emailFile.txt', 'w')
        f.write(
            f"""
            to: {to}
            subject:{subject}
            bodyreceiver_name:{bodyreceiver_name}"""
        )
        f.close()

class Office():
    def __init__(self, name):
        self.id = id
        self.name = name
        # self.employees = employees
    
    def get_all_employees(self):
        print("gelling all employees")
        mydb=DBConnection()
        print(mydb.dbGetAllEmployees());
    def get_employee(self,id):
        print(f"getting employee:{id}")
        mydb=DBConnection()
        print(mydb.dbGetEmployee(id));
    def fire(self,empId):
        print("firing")
        mydb=DBConnection()
        print(mydb.dbDeleteEmployee(empId));
    def hire(self,Employee):
        print("hiring")
        mydb=DBConnection()
        print(mydb.dbInesrtEmployee(Employee));

emp =Employee("amal",2000,"very good",60,"good","true","amal@gmail.com",2000)
myOffice=Office("ITI_office")
# myOffice.get_all_employees()
# myOffice.get_employee(1)
myOffice.hire(emp)
myOffice.fire(emp.id)


