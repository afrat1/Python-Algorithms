# Create an algorithm that will return True if the two integer values you get from the user are equal or the difference of these numbers is a multiple of 5.

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first == second or abs(first - second) % 5 == 0:
    print("True!")
else:
    print("False!")

print(first == second or abs(first - second) % 5 == 0)