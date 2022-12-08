x1,y1=eval(input("Enter coordinates of top left vertex of rectangle(separeted by comma): "))
x2,y2=eval(input("Enter coordinates of bootom right vertex of rectangle(separeted by comma): "))
x,y=eval(input("Enter coordinates of point(separeted by comma): "))

if(x<x1 and y<y1 and x>x2 and x>y2):
    print("point lies inside rectangle")
else:
    print("point lies outside the rectangle")