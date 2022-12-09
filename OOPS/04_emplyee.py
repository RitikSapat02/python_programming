class employee:
    company = "Google"     #classs attribute
    salary = 100
harry = employee()
rajni = employee()
print(harry.company)
print(rajni.company)


employee.company = "Microsoft"            #you can change it
harry.company = "Facabook"             
print(harry.company)
print(rajni.company)

#instance attribute: 
# harry.salary = 300
# rajni.salary = 400
print(harry.salary)
print(rajni.salary)