def main():
    price = 50
    total_paid = 0
    vending_machine(price, total_paid)


def vending_machine(price, total_paid):
    while price > 0:
        print(F"Amount due: {price}")
        pay = int(input("Insert a coin: "))
        
        if pay == 25 or pay == 10 or pay == 5:
            price = price - pay
            total_paid = total_paid + pay
        else:
            print("NOT a coin!")
        
    if total_paid >= 50:
        print("THANKS! Here's your coke")
        print(f"Here's your change: {total_paid - 50}")

main()