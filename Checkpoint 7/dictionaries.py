#key : value                                                #a dictionary in python works like this
# capitals = {                                                #dictionaries work with CURLY BRACES {}
#     "Mexico": "Mexico City",
#     "Canada": "Ottawa",
#     "Brazil": "Brasilia"
#     #"Canada": "Montreal"                                       # use UNIQUE keys
# }

# capitals["Italy"] = "Rome"                                  #to ADD a new element to the dictionary
# del capitals["Brazil"]                                      # del is to DELETE an element 
# capitals.pop("Canada")                                        #.pop is another METHOD to delete an element
# capitals.clear()                                    #it CLEARS the entire list of elements in the dictionary. Use empty parentheses.

#print(capitals)                                   #[] to access a SPECIFIC value in the dictionary

#Exercise 1
# houses = {
#     "Hermione": "Griffindor",
#     "Harry": "Griffindor",
#     "Ron": "Griffindor",
#     "Draco": "Slytherin"
# }
# for students in houses:                                              #python will go through each key 
#     print(f"{students}: {houses[students]}")                         #accesing the value using the key


#Complex dictionary
students = [
    { "name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    { "name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    { "name": "Ron", "house": "Griffindor", "patronus": "Jack Russell Terrier"},
    { "name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print(f"{student["name"]}, {student["house"]}, {student["patronus"]}")