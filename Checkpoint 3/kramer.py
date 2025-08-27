greeting = input("Type a greeting: ")

if greeting.startswith("Hello"):
    print("$0")
elif greeting.startswith("H"):
    print("You have won $20")

else:
    print("CONGRATULATIONS! YOU HAVE WON $100")
