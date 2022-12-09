from re import L


t = (1,2,3,4,5,6,"strig")
l = list(t)
l.remove(2)
t = tuple(l)
print(t)


#delete tuple
del t
