# Create an algorithm that finds BMI

w = int(input("Please enter your weight in kg: "))
h = int(input("Please enter your height in cm: "))

result = round(w / ((h/100) ** 2),2)
print(result)

if result < 18.5:
    body = "underweight"
elif result < 25:
    body = "normal"
elif result < 30:
    body = "overweight"
elif result < 35:
    body = "obese"
else:
    body = "extremely obese"
print(f"Your bmi is: {result} and your body type is: {body}") 