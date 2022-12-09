class student:
    totalstudents= 20

    def sayhello():
        print("Hello")

    def printName(self):
        name = "Local name"
        print(self.name)
        print(name)

s1 = student()
s1.name = "Ritik"
s1.printName()      #student.printName(s1)



