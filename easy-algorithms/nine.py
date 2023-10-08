# Write python code that extracts the phone number in a given string expression.

given_str = "My phone number is (111) 222-33-44"

numbers = [char for char in given_str if char.isdigit()]

my_string = ""
for number in numbers:
    my_string += number

print(my_string)

# 2.çözüm

output = ""

for i in given_str:
    if i in "012345789":
        output += i

#for i in given_str:
#    if i.isnumeric():
#        output += i

print(output)