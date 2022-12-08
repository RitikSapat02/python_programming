x,y=eval(input("Enter coordinates of center separeted by comma: "))
x1,y1=eval(input("Enter coordinates of Point separeted by comma: "))
r=eval(input("Enter radius: "))

d=((x1-x)**2 + (y1-y)**2)**0.5
if(r>d):
    print("Point lies inside the circle")
elif(r<d):
    print("point lies outside the circle")
else:
    print("point lies on the circle")