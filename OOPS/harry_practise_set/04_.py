class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,com2):
        return complex(self.real+com2.real,self.imag+com2.imag)
    
    def __mul__(self,com2):
        mulreal = (self.real*com2.real) - (self.imag*com2.imag)
        mulimag = (self.real*com2.imag)+(self.imag * com2.real)
        return complex(real=mulreal,imag=mulimag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = complex(1,2)
c2 = complex(2,3)
print(c1+c2)
print(c1*c2)