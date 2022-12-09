#strings can be written in 3 ways
'''a ='string'
b = "string"
#c = '''#string
#is'''
#print(a,b,c)
'''

'''#indexed
#print(a[3])

#immutable
'''a[3] = "r"  '''  #error


'''
#string concatination
print(a+"Str")
b="p"
b = b*3
print(b)
'''

'''
#string slicing
st = a[1:3]
print(a[1:5:2])
print(st)
'''

'''

#iterating_over_string
str = "Hello World"
count = 0
for x in str:
    if x=='l': count+=1
print(count)
'''

'''

str = "hello world"
count = 0
for x in str:
    if (x=='l') :count+=1
print(count)

'''

'''
#comaprison operators on string
a = "parikh"
b = "ratik"
print(a=="parikh")
print(a>b)
print(a<b)
'''


#string operations
str ="Hello"
print(len(str))

print(str.endswith("lo"))

print(str.startswith("h"))

print(str.replace("H","w"))

print(str.find('l'))

print(str.lower())

print(str.strip())