class EMployee:
    company = "Bharat gas"
    salary = 5600
    salarybonus = 400 

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary

e = EMployee()
print(e.totalsalary)

print(e.salarybonus)
e.totalsalary = 5800
print(e.salarybonus)
print(e.totalsalary)