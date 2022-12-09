x1,y1=eval(input("Enter x and y coordinates of 1st point: "))
x2,y2=eval(input("Enter x and y coordinates of 2nd point: "))
distance=((x2-x1)**2 + (y2-y1)**2)**0.5
print("The distance between two points is: ",round(distance,2))