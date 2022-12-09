a = input()
def check(str):

    v,c,d,s = 0,0,0,0
    for x in a:
        if(x>='a' and x<='z' or x>='A' and x<='Z'):
            x=x.lower()
            if(x in ['a','e','i','o','u']):
                v+=1
            else:
                c+=1
        elif(x >= '0' and x <= '9'):
            d+=1
        else:
            s+=1
    return v,c,d,s

print(check(a))
   