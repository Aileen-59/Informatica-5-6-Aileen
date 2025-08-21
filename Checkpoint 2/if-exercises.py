def main():
    number = int(input("Write an integer number: "))
    if number < 0:
        print(number * -1)
    if number > 0:
        print (number)
        
        
main()   

#Exercise 2
def main():
    number1 = int(input("First number: ")) 
    number2 = int(input("Second number:"))
    op = int(input("Write an operation: "))
    addition = number1 + number2
    multiplication = number1 * number2
    substraction = number1 - number2
    operation(number1, number2, op,addition, multiplication, substraction)
    
    
def operation(op, add, multiplication, substract):
    if op == addition:
        print(int addition)
        