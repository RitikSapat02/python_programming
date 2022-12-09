#line-separated input
'''
l = []
a = int(input())                     
for x in range(a):           
    l.append(int(input()))       

print(l)
'''


#space-separated as string
'''l = input().split(",")      #delimeter = ,
print(l)    '''                       

#space-separated as int
l = input().split()
newlist = []
for x in range(len(l)):
    newlist.append(int(l[x]));
print(newlist)
