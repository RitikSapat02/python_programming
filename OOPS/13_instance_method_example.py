class student:
    name = "jatin"

    def say_hi(self):
        print("hello , my name is",self.name)
    

p = student()
p.say_hi()  
r= student()
r.name = "Ritik"
r.say_hi()