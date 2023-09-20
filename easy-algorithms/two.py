# Write a Python program to return a string consisting of the first 3 and the last 3 characters of a string you received from the user.
# If string length is less than 3, return "empty string".

a = input("Enter your string: ")

if len(a) < 3:
    print("empty string")
else:
    print(a[:3] + a[len(a)-3 : len(a)])

# a[len(a)-3 : len(a)] == a[-3:0]