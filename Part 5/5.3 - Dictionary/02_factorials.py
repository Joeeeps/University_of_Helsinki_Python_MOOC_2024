# Write your solution here
def factorials(n: int):
    result = {}
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i-1] * i
    return result

 
if __name__ == "__main__":
    d = factorials(5)
    print(d[1])
    print(d[3])
    print(d[5])
