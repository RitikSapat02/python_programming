class Employee:
    company = "visa"
    ecode = 20

class freelancer:
    company = 'fiverr'
    level = 0

    def upgradelevel(self):
        self.level+=1

class programmer(Employee , freelancer):
    name = "Rohit"

p = programmer()
p.upgradelevel()
print(p.level)
print(p.company)
print(freelancer.level)
