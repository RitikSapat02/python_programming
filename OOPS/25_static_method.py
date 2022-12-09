class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll


    @staticmethod
    def greet():
        print("Good Morning!!")
    
s1 = student("Ritik",54)
s1.greet()
student.greet()