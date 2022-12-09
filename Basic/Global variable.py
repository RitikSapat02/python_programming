a=10 #global variable
b=69 #global
c=2 #global
def function():
    a=5 #local
    global c #now we can change value of global c here and that reflect in rest of the program
    c=25
    print(b) #global b is use in function
    print(a)
    print(c)
    

function()
print(a)
print(c)
print(function())