# Write your solution here

person1 = input("Name: ")
age1 = int(input("Age: "))

person2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {person1}")
elif age2 > age1:
    print(f"The elder is {person2}")
elif age1 == age2:
    print(f"{person1} and {person2} are the same age")
