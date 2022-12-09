class dog:
    tricks = []
    def __init__(self,name):
        self.name = name
    
    def add_trick(self,trick):
        self.tricks.append(trick)

a = dog('Bruno')
b = dog('maxx')
a.add_trick("eat")
a.add_trick("talk")

print(a.tricks)
print(b.tricks)

print(id(a.tricks))
print(id(b.tricks))