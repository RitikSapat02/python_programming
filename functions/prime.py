def prime(a):
    for i in range(2,a):
        if(a%i==0):
            return "Not prime"
    else:
        return "prime"

n=int(input())
print(prime(n))
    