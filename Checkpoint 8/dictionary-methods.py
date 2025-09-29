dictionary = {
    "color": "blue",
    "age": 16
}

#Valuessss
print(dictionary.values())
for v in dictionary.values():
    print(v)

#Keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)
    
#Items
print(dictionary.items())
for i in dictionary.items():
    print(i)
    
#Print key and value using methods
#TO DO 

#Get method
picnic_items ={"apples": 5, "cups": 2}
print(f"I'm bringing {picnic_items.get("cups")} cups.")

print(f"I'm bringing {picnic_items.get("eggs", 0)} eggs.") #if eggs is not found, return 0 instead of None

#Setting Default Values
pet_info = {
    "name": "Cody",
    "age": 2
}
pet_info.setdefault("color", "black")                   #if color is not found, set it to black
print(pet_info)