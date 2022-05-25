from DB_Handler import DBConnection
from EmployeeClass import Employee
class Office():
    def __init__(self, name):
        self.id = id
        self.name = name
        # self.employees = employees

    def showEmployee(self,Employee):
        #Employee.is_manager
        if(Employee[5]):
            print(f"""
            ID:{Employee[0]} , Name:{Employee[1]} , money:{Employee[2]} , sleep mood:{Employee[3]},health Rate:{Employee[4]},Is Manager:{Employee[5]},salary:Hidden,email:{Employee[7]}
            """)
        else:
          print(f"""
            ID:{Employee[0]} , Name:{Employee[1]} , money:{Employee[2]} , sleep mood:{Employee[3]},health Rate:{Employee[4]},Is Manager:{Employee[5]},salary:{Employee[6]},email:{Employee[7]}
            """)

    
    def get_all_employees(self):
        print("gelling all employees")
        mydb=DBConnection()
        empArray=mydb.dbGetAllEmployees()
        for emp in empArray:
            self.showEmployee(emp)

            
        
    def get_employee(self,id):
        print(f"getting employee:{id}")
        mydb=DBConnection()
        emp=mydb.dbGetEmployee(id)
        self.showEmployee(emp[0])

    def fire(self,empId):
        print("firing")
        mydb=DBConnection()
        print(mydb.dbDeleteEmployee(empId));

    def hire(self,Employee):
        print("hiring")
        mydb=DBConnection()
        print(mydb.dbInesrtEmployee(Employee));
   