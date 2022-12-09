a=()   #empty tuple
print(type(a))
a=(1)
print(type(a))

a=(1,) #tuple with one element
print(a)

b=(1,2,3,44,5,5,23,212,1,3)
# b[4]=4;       Error
print(b)


#tuple methods
print(b.count(1)) #returns no of times 1 occured in b
print(b.index(212)) #returns index of first occurnce of specied value