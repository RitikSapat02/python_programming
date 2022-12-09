class student:
    def setName(self,name):
        self.name = name

    def getName(self):
        print(self.name)

    def setClassattr(room):
        student.room = room;

s1 = student()
s1.setName("Shikhar")
s1.getName()

print(student.__dict__)
student.setClassattr(23)
print(student.__dict__)