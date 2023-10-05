#If the two object received from the user are of an integer type, write a Python program to sum the two objects.

x,y = input("Enter the numbers with comma: ").split(",")

if x.isnumeric() and y.isnumeric():
    print(int(x) + int(y))
else:
    print("False")
