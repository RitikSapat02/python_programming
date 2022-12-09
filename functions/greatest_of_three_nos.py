def great(a=0,b=0,c=0):
    if(a>=b):
        if(a>=c):
            return a
        else:
            return c
    else:
        if(b>=c):
            return b
        else:
           return c

print(great(4,54,6))