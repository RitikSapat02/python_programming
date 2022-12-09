n=int(input())
r=int(input())
def factorial(a):
    factorial=1
    for i in range(2,a+1):
        factorial*=i
    return factorial
n_fact=factorial(n)
r_fact=factorial(r)
n_r_fact=factorial(n-r)

print(n_fact//(r_fact*n_r_fact))