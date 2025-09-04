def main():                                                     #main function
    user_message = input("Type a message: ").lower()           #user input
    encode_message(user_message)                               #To know what we want to encode
    
def encode_message (text):                                    #function to encode the message 
    alphabet = "abcdefghijklmnopqrstuvwxyz"                    #alphabet defined
    cipher = "zyxwvutsrqponmlkjihgfedcba"                      #alphabet reversed
    new_message = ""                                            # to write the new message
    i = 0                                                       #To start from 0 and go through the alphabet

    while i < len(text):                                        #while loop
        char = text[i]                                          #To put each character in its given position

        if char in alphabet:                                    #To check if the character is in the alphabet
            cipher_index = alphabet.find(char)               #To find the index of the character
            new_message += cipher[cipher_index]               #Put the character in a new message
        else:                                                   #If the character is not in the alphabet:
            new_message += char                                 #keep the character as it is
        i += 1                                                      #go to the next character
    print(new_message)                                           #print the new message

main()                                                              #go to the main function 
