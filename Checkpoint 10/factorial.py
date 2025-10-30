# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero.")
#     return a / b

# print(divide(1,2))
# print(divide(2,0))

def main(): 
    print("Factorial Calculator")
    integer = int(input("Enter a positive integer: "))
    print(f"{integer}! = {factorial(integer)}")

def factorial(n):
    if n < 0:
        raise ValueError(f"The input was negative or zero: {n}")
    else:
        new_n = 1
        for i in range(2, n +1): 
            new_n = new_n * i 
            return new_n
        
                  
    
main()