def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
        
    print(dictionary)
    
    print(sum(dictionary.values()))

    #Alternative 1
    values_list = list(dictionary.values())
    print(values_list)
    largest_number_index = values_list.index(max(values_list))
    repeated_character = list(dictionary.keys())[largest_number_index]
    print(f"The most repeated character is {repeated_character}, repeating {dictionary[repeated_character]} times.")
    
    #Alternative 2
    largest_number2 = max(dictionary, key=dictionary.get)
    print(f"The most repeated character is {largest_number2}, repeating {dictionary[largest_number2]} times.")

#print(list(character_counter.keys()[list(character_counter.values()).index(max(character_counter.values()))]))

message = input("Enter a message: ") 
dictionary = {}
character_counter(message, dictionary)