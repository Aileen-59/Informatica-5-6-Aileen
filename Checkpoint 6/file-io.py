#names = []

#for i in range(3):
#    name = input("Enter a name: ")
#    names.append(name)

#for name in sorted(names):
#    print(f"Hello, {name}")

name = input("What is your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()