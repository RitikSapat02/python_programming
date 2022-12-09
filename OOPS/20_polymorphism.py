class user(object):
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("Do nothing")

class wizard(user):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"attacking with power of {self.power}")


class archer(user):
    def __init__(self,name,num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f"attacking witharrow:arrow left--{self.num_arrow}")

wizard1 = wizard("merlin",60)
archer1 = archer('Robin',30)

def player_attack(char):
    char.attack()

for i in [wizard1,archer1]:
    print(type(i))
    player_attack(i)