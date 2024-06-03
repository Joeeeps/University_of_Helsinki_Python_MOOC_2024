# Copy here code of line function from previous exercise
def line(number:int, string:str):
    if string == "":
        string = "*"
    print(number*string[0])
        
def square(size, character):
    # You should call function line here with proper parameters
    sizeOG = size
    while size > 0:
        line(sizeOG, character)
        size -= 1 
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
