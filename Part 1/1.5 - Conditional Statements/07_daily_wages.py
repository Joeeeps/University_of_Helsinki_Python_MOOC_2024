# Write your solution here
hour = float(input("Hourly wage: "))
worked = float(input("Hours worked: "))
day = input("Day of the week: ")

if day != "Sunday":
    print(f"Daily wages: {hour*worked} euros")

if day == "Sunday":
    print(f"Daily wages: {(hour*worked)*2} euros")



