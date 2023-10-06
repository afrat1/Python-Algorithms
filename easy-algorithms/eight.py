# Write a program that takes a country's name and its area as arguments and returns the are of the country's proportion of the total world's landmass.

country = input("Enter country name: ")
area = input("Enter the are of the country: ")

earth = 148940000

yuzde = round((int(area) / earth) * 100,2)

print(f"{country} is {yuzde} % of the total world' landmass.")
