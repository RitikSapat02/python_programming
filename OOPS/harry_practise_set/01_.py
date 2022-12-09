class vector2d:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j 
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    

class vector3d(vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v = vector2d(2,3)
v1 = vector3d(3,4,5)
print(v)
print(v1)