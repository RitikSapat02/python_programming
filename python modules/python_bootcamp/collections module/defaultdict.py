from ast import Lambda
from collections import defaultdict

#----Normal dictionary----
d = {'a' : 1}
print(d['a'])
#print(d["ritik"])       #error


#----default detionary---

d = defaultdict(lambda : 0)
d['correct'] = 100
print(d['correct'])

print(d['Wrong key'])
print(d)