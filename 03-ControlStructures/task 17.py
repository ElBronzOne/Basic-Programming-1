x = int(input("etner the first(x) coordinate"))
y = int(input("enter the second(y) coordinate"))
if x == 0:
    print("the point is set on the y axis")
elif y == 0:
    print("the point is set on the x axis")
elif x>0 and y>0:
    print("the point is in the first quadrant")
elif x>0 and y<0:
    print("the point is in the fourth quadrant")
elif x<0 and y<0:
    print("the point is in the third quadrant")
elif x<0 and y>0:
    print("the point is in the second quadrant")