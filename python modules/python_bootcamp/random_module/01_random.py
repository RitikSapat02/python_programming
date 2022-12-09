import random
a = range(20)
print(a)
li = list(a)
print(li)
random.seed(0)
print(random.choice(li))
print(random.uniform(a=0, b=100))
print(random.gauss(mu=0,sigma=1))
