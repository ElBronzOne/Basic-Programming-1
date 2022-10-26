first = int(input("enter first number: "))
second = int(input("enter second number: "))
if first > second:
    print(f"numbers in ascending order: {second} {first} ")
if first < second:
    print(f"numbers in ascending order: {first} {second} ")
if first == second:
    print(f"numbers are equal {first} = {second} ")
else:
    print("error while entering data ")