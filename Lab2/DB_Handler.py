import mysql.connector
 
class DBConnection():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "PythonDB"
    )
 
 
    def dbGetAllEmployees(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM `Employee`")
        myresult = cursor.fetchall()
        return myresult

    def dbGetEmployee(self,id):
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT * FROM `Employee` WHERE `id` = {id}")
        employee = cursor.fetchall()
        return employee
    
    def dbInesrtEmployee(self,Employee):
        cursor = self.mydb.cursor()
        cursor.execute(f"""
        INSERT INTO Employee (full_name, money,sleepmood,healthRate,salary,email)
        VALUES ('%s', %s, '%s', %s, %s, '%s');
        """% (Employee.full_name, Employee.money, Employee.sleepmood ,Employee.healthRate, Employee.salary , Employee.email)
        )
        self.mydb.commit()
        print(cursor.rowcount, "record inserted.")
        # print(cursor)
        # return employee
    
    def dbDeleteEmployee(self,id):
        cursor = self.mydb.cursor()
        cursor.execute(f"DELETE FROM `Employee` WHERE `id` = {id}")
        employee = cursor.fetchall()
        return employee

db=DBConnection()
# print(db.dbGetAllEmployees())
# print(db.dbGetEmployee(1))
        
