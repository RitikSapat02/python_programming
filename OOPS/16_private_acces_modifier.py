class student:
    __total = 20
    def __init__(self,name,roll):
        self.__name = name
        self.roll = roll
    
    def getName(self):
        print(self.name)
    
    def __setName(self,name):
        self.__name = name
    
    def password(self,passWord,name):
        if(passWord=="ABC"):
            self.__setName(name)

    def __str__(self):
        return f"Details:\n  name: {self.__name}\n  roll: {self.roll}"

s1 = student("Rohit",54)
print(s1)

#print(s1.name)                        #Error
#s1.setName("Admin")                    #Error
print(s1.__dict__)                    
s1.name = "Rahul"                       #this will add one more instance attribute
s1.password("ABC","Admin")
print(s1)

print(s1.__dict__)

#acessing to private variable            Actually nothing is private in python
print(s1._student__name)
print(student._student__total)