

gender=input("Enter your gender (M,m,F,f): ")
sal=int(input("Enter salary:"))


bonus=0
Total_salary=0
if(gender=="M" or gender=="m"):
        bonus=bonus+0.5*sal

elif(gender=="F" or gender=="f"):
        bonus=bonus+0.1*sal

else:
        print("Plz input valid gender\n")
    
if(sal<=10000):
        bonus=bonus+0.2*sal
Total_salary=sal+bonus
print("\n*************************\n")
print("Your salary:",sal,"\nBonus:",bonus,"\nTotal_salary:" ,Total_salary)
    