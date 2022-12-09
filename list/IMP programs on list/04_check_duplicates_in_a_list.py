def checkDuplicate(l):
    newlist = []
    for x in l:
        if(l.count(x) > 1):
            if x not in newlist:
             newlist.append(x)
    return newlist

print(checkDuplicate([1,23,4,2,12,4,2,5,5,3,10,1]))
