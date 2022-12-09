def fun(init_sum,*num):
    sum=init_sum
    for i in num:
        sum+=i
    return sum

print(fun(4,56,7,6))