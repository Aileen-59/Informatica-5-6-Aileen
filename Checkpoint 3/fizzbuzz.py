def main():
    number = input("Write a number:")
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("FizzBuzz!!!!")
    
    elif int(number) % 3 == 0:
        print("FIZZ!")
    elif int(number) % 5 == 0:
        print("BUZZ!")

    
main()