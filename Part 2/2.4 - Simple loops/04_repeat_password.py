# Write your solution here
pin=4321 
attempts = 0

while True: 
    code = int(input("Pin: "))
    attempts = attempts + 1
    if code == 4321 and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif code != 4321:
        attempts == attempts + 1 
        print("Wrong")
    elif code == 4321 and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break
