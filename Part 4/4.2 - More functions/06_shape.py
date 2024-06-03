# Copy here code of line function from previous exercise
def line(number:int, string:str):
    if string == "":
        string = "*"
    print(number*string[0])
    
def shape(size1, character1, size2, character2):
    # You should call function line here with proper parameter
    num = 0
    sizeOG = size1
    while size1 > 0:
        num += 1
        line(num, character1)
        size1 -= 1 
    num = 0 
    while size2 > 0:         
        line(sizeOG, character2)
        size2 -= 1
        
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    
    
