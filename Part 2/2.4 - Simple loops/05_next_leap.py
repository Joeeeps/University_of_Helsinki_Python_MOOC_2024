# Write your solution here
year = int(input("Please type in a year:"))
nextleap = year 
leap = False

while True:
    nextleap += 1 # keep adding values till we hit leap criteria 
    if nextleap % 4 == 0 and nextleap % 100 != 0:
            leap = True
            break
    elif nextleap % 4 == 0 and nextleap % 100 == 0 and nextleap % 400 == 0: 
        leap = True
        break 

print(f"The next leap year after {year} is {nextleap}")



