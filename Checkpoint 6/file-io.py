#names = []

#for i in range(3):
#    name = input("Enter a name: ")
#    names.append(name)                                                     # to add to the list

#for name in sorted(names):                                                 # to sort the list alphabetically
#    print(f"Hello, {name}")

# Exercise 2
# name = input("What is your name? ")
# file = open("names.txt", "a")                                             #"a" will add to the file
# file.write(f"{name}\n")                                                  # to add a new line after each name
# file.close()                                                                  #to close the file

#Exercise 3
# with open("names.txt", "a") as file:                                   #"a" will add to the file
#     file.write(f"{input("What's your name? ")}") 


# Exercise 4
with open("names.txt", "r") as file:                                    # "r" will read the lines of the file
    lines = file.readlines()
    
    for line in lines:
        print(f"Hello, {line.rstrip()}")                                #rstrip() removes spaces to the right. 