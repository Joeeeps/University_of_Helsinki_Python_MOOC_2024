# Write your solution here

temp = int(input("Please type in a temperature (F): "))
celsius = (temp-32)*5/9

if celsius < 0:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")

if celsius >= 0:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")

