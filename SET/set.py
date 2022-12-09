s = set()    #empty
s = {}      #empty dict

s={"apple","abs",12}
#print(a[0])      #error
print('abs' in s)

#looping
for x in s:
    print(x)

#methods
print(len(s))

s.add(9)
print(s)

s.update([1,2,3,3,3,3])
print(s)

s.remove(3)
print(s)

s.pop()
print(s)