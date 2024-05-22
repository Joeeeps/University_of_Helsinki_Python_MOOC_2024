# Write your solution here
limit = int(input("Limit: "))
nummy = 1 
nommy = 2 
nommychain = str(nummy)

while limit > nummy:
    nummy += nommy
    nommychain = nommychain + " + " + str(nommy)
    nommy += 1

print(f"The consecutive sum: {nommychain} = {nummy}")
