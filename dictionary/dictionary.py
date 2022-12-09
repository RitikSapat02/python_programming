a = {} #empty
print(type(a))

a = {
    'c':3,
    "string":"ritik",
    "harry":"100",
    'list':[1,2,3,4]
    }
print(a)

#copy dictionary
b = a.copy()

d = dict([(1 ,4),('string',"ritik"),("haaryy","coder")])
print(b,d)

#use fromkeys to create dictionary

e = dict.fromkeys(["abs",12,34])
print(e)

#access dict
print(a["string"])

#dictinary Methods
print(a.get("string"))
print(a.values())
print(a.keys())
print(len(a))
a.update({"friend":"sam",
1:3})
print(a)

a.pop(1)

a.popitem()
print(a)

a.clear()
print(a)

#looping
a ={
    'c':3,
    "string":"ritik",
    "harry":"100",
    'list':[1,2,3,4]
    }

for i in a:
    print(i)        #keys

for i in a:
    print(a[i])

for i in a.values():
    print(i)

for d,s in a.items():
     print(d,s,sep="-")