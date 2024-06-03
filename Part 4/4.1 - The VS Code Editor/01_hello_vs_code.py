# Write your solution here
editor = input("Editor: ")

while True:
    if editor.lower() == "visual studio code":
        print("an excellent choice!") 
        break
    elif editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
        editor = input("Editor: ")
    else:
        print("not good")
        editor = input("Editor: ")

