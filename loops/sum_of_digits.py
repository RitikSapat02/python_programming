n=int(input())
sum=0
while(n):
    rem=n%10
    n=n//10
    sum+=rem

print(sum)