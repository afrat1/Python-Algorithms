# Write a Python program to display your details like name, age, job in three different lines

# score = "90,99,100,85,92"
# print(score.split(","))

per = input("Please enter your name, age and job seperating them with comma: ").split(",")  
print("name: ", per[0])  
print("age: ", per[1])  
print("job: ", per[2])  

print(f"name: {per[0]} age: {per[1]} job: {per[2]}")