# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
d = (b**2) - (4*a*c)  
#positive discriminant = two distinct solutions
#zero = one solution
#negative = no real solutions

# Check the value of the discriminant and find the solutions accordingly
if d > 0:
    # Two distinct real solutions
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"The roots are {x1} and {x2}")

if d == 0:
    # One real solution (repeated root)
    x = -b / (2 * a)
    print("The root is {x}:")

if d < 0:
    print("No real solutions")

