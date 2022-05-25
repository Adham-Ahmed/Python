from random import randint
import re;
from DB_Handler import DBConnection
from PersonClass import Person
import uuid
# id = uuid.uuid4()
class Employee(Person):
    # id=10
    salary=0;
    def __init__(self,full_name,money,sleepmood,healthRate,workmood,is_manager,email,salary):
       super().__init__(full_name,money,sleepmood,healthRate)
    #    self.id = randint(1,10000)
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
            print("salary should be 1000 and more")

    def getSalary(self):
        return self.salary;
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




