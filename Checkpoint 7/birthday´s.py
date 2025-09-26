birthdays = {
    "Shensi" : "March 9",
    "Melissa": "March 15",
    "Renata" : "March 29"
}

name = input("Who's birthday do you want to look up?: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don't have {name}'s birthday")
    new_birthday = input(f"When is {name}'s birthday?:")
    birthdays[name] = new_birthday
    print("Birthday added")
print(birthdays)