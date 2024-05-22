# Write your solution here
string = input("Please type in a string: ")
nom = 0
nommy = ""
while nom < len(string):
    nom += 1 
    nommy = string[-nom] + nommy 
    print(nommy)
