income=eval(input("Enter your income: "))
tax=0.0
if(income>=250000 and income<=500000):
    tax=tax+0.05*(income-250000)
if(income>500000 and income<=1000000):
    tax=tax+0.2*(income-500000)
if(income>1000000):
    tax=tax+0.3*(income-1000000)

print("Income tax: ",tax)