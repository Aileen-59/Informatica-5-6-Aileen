while True:

    greeting = input("Type a greeting: ")

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("You have won $20")

    else:
        print("CONGRATULATIONS! YOU HAVE WON $100")
        break
