import getpass

def main():
    password = getpass.getpass("Set a password:")
    input("Press enter to continue.")
    check_password(password)
    
    
def check_password(p):
    guess = input("Enter password:")
    if p == guess:
        print("You knew the password")
    
    
    if p != guess:
        print("Incorrect password")
    print("The program has ended")   

main()