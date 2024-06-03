# Copy here code of line function from previous exercise
def line(number:int, string:str):
    if string == "":
        string = "*"
    print(number*string[0])
        
def triangle(size):
    # You should call function line here with proper parameter
    num = 0
    while size > 0:
        num += 1
        line(num, "#")
        size -= 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

