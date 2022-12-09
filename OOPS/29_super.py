class person:
    contry = "India"
    def __init__(self):
        print("person is initializing!")

    def takebreath(self):
        print("I am breathing!")

class Employee(person):
    company ="Honda"

    def __init__(self):
        super().__init__()
        print("Employee is initializing!")
    def takebreath(self):
        super().takebreath()
        print("I am an Employee so I am luckily breathing!!")

class programmer(Employee):
    company = 'fiverr'
    def __init__(self):
        super().__init__()
        print("Programmer is initializing!")

    def takebreath(self):
        super().takebreath()
        print("I am a programmer so I am breathing!!")

# p = person()
# e = Employee()
pr = programmer()

# pr.takebreath()