def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")

 #this makes a function looking for the persons name

def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
    print("ok!")
 
 #this makes the persons[name] into an empty list, and then appended to get potentially numerous number values
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
#this allows the third definition to rely on functions

main()

# Write your solution here
