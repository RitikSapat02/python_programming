class Animal:
    category = "animal"
    def shout(self):
        print("I am shouting!!!!")

    def who_are_u(self):
        print("I am animal!!!")

class dog(Animal):
    pass

d = dog()
print(d.category)
d.shout()
d.who_are_u()