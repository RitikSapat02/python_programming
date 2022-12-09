class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class dog(Animal):
    def __init__(self):
        print("dog created")
    def who_am_i(self):
        print("I am a dog!")

mydog = dog()
mydog.eat()
mydog.who_am_i()
