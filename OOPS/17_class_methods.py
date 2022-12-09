from types import ClassMethodDescriptorType


class student:
    __totalstudents = 20

    @classmethod
    def getTotalStudents(cls):
        return cls.__totalstudents
        
print(student.getTotalStudents()) #student.getTotalstudents(student)


class playerCharacter:
    membership = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def shout(self):
        pass

    @classmethod
    def adding_nos(cls,num1,num2):
        return num1+num2

print(playerCharacter.adding_nos(5,5))          #  playerCharacter.adding_nos(playerCharacter)
