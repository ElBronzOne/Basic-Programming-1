def f(number1, number2, number3):
    x=0
    y=0
    print(number1,"|",number2,"|",number3)
    x=number1
    if number2>x:
        x=number2
    if number3>x:
        x=number3
    y=number1
    if y>number2:
        y=number2
    if y>number3:
        y=number3
    print(x,"|",y)
    return x-y
    
# from random import randrange
# for x in range(30):
#     print(f((randrange(10)),(randrange(10)),(randrange(10))))
print(f(9,9,9))