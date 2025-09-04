def main():
    number = int(input("Enter a positive number: "))
    table(number)
    
def table(number):
    i = 1
    while i <= 10:
        multiplication = number * i
        print(f"{number} x {i} = {multiplication}")
        i += 1
    
main()