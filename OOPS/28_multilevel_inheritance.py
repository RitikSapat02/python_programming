class person:
    contry = "India"

    def takebreath(self):
        print("I am breathing!")

class Employee(person):
    company ="Honda"

    def takebreath(self):
        print("I am an Employee so I am luckily breathing!!")

class programmer(Employee):
    company = 'fiverr'
    def takebreath(self):
        print("I am a programmer so I am breathing!!")

p = person()
e = Employee()
pr = programmer()
print(p.contry)