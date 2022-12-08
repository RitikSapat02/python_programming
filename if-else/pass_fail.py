a,b,c,=eval(input("Enter three subjects marks separeted by comma: "))
percent=(a+b+c)/3
if(a>=33 and b>=33 and c>=33 and percent>=40):
    print("You are pass and got percen: ",percent)
else:
    print("You are fail and got percentage: ",percent)
