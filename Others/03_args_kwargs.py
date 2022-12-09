def super_fun(a,b,*args,c=10,d=0,**kwargs):
    whole_sum = sum(args)+a+b+c+d
    for x in kwargs.values():
        whole_sum+=x;
    return whole_sum

print(super_fun(2,3,3,4,5,5,p=2,r=7))