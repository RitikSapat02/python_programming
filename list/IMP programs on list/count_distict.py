def distict(l):
    res=1
    for i in range(len(l)):
        if(l[i] not in l[:i]):
            res+=1
    return res

l = [1,2,3,4,2,2,13,3]
print(distict(l))

#2nd way
l1 = [1,2,3,4,4,3,2,3,134,4,2,5,7]
s = set(l1)
print(len(s))