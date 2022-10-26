
speed = int(input("enter the current car speed as an integer vlaue  "))
t = Timer(1, speed+1)
t.start() 
points = (speed - 130)/4
if speed >= 130:
    print("you exceedeed the speed limit gimme your driving license points at the value of ", points)
if speed == 200:
    cancel(	)
    print("you crashed boi")
    
else:
    print("u good homie")
