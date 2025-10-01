def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
        
    print(dictionary)
    print(len(dictionary))

#print(list(character_counter.keys()[list(character_counter.values()).index(max(character_counter.values()))]))

message = input("Enter a message: ") 
dictionary = {}
character_counter(message, dictionary)