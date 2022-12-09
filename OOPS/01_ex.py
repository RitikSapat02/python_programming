class Number():
    def sum(self):
        return self.a + self.b

num = Number()            #object instatiation
num.a =12
num.b =34
s = num.sum()
print(s)