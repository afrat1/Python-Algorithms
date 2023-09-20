#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "sari"
s2 = "mehmet"

a = s1[0:2]
b = s1[2:4]

s3 = a + s2 + b

print(s3)

a = s1[:len(s1) // 2]
b = s1[len(s1) // 2:]

print(s3)