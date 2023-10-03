# Create an algorithm that asks the employee for weekly working hours and hourly wage information and
# ultimately calculates the employee's weekly salary.

# Note >> Work over 40 hours per week is paid 1.5 times the wage.

work_hours = int(input("work hours: "))
hourly_wage = int(input("hourly wage: "))

if work_hours <= 40:
    result = work_hours * hourly_wage
else:
    result = (work_hours - 40) * (hourly_wage * 1.5) + (40 * hourly_wage)

print(f"Your weekly wage is {result}")