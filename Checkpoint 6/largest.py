def main():
    list_length = int(input("List length: "))
    numbers = []
    
    for i in range(list_length):
        list_element = int(input("Enter a number: "))
        numbers.append(list_element)
    print(numbers)
    
    with open("numbres.txt", "a") as file:
        for number in numbers:
            file.write(f"{number}\n")
    print(f"The largest number is {max(numbers)}")

main()