t = (1,2,3,"string")        #packing
# a,b,c,d =t                 #unpacking
# print(a,b,c,d)


a,*b = t                 #use * if no of variables is less
print(a,b)

*a,b = t
print(a,b)