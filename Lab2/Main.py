from EmployeeClass import Employee
from OfficeClass import Office
myOffice=Office("ITI_office")
def printMenu():
    print("""
    1)Hire Employee
    2)Fire Employee
    3)get Employee
    4)get All Emplpoyees
    """)

def createEmployee():
    name=input("name:")
    money=int(input("money:"))
    sleepmood=input("sleep Mood:")
    health=int(input("health Rate(0-100):"))
    workMood=input("work Mood:")
    Ismanager=input("Is manager(True , False):")
    email=input("email:")
    salary=int(input("salary:"))
    return Employee(name,money,sleepmood,health,workMood,Ismanager,email,salary)
    
inputx=0
while(inputx !=  'q'):
    printMenu()
    inputx=input("Please Enter the corresponding number ( q to quit): ")
    if(inputx == 'q'):
        break;

    if(inputx=='1'):#hire 
        emp=createEmployee()
        myOffice.hire(emp)
        
    if(inputx=='2'):#fire
        idtoFire=input("Please enter the Id of the Employee to fire:")
        myOffice.fire(idtoFire)
        
    if(inputx=='3'):#get Employees
        idToShow=input("Please enter the ID of the employee to show :")
        myOffice.get_employee(idToShow)

    if(inputx=='4'):#get All Employees
        print("option 6")
        myOffice.get_all_employees()

