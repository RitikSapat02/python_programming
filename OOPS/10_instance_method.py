class student:
    #class attribues
    totalStudents = 20
    classTeacherName = "aish"

    #instance methods
    def printHello(self):
        print("Hello")

s1 = student()
# s1.printHello()       ## same as ''' student.printHello(s1)
student.printHello(s1)