class Employee:
    company = "Google"
    def getSalary(e):              #e = self =etc 
        print("Salary is 100k")

harry = Employee()
harry.getSalary()
Employee.getSalary(harry)
