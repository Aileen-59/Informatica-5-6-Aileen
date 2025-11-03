# import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# cards =["jacks", "queens", "kings", "aces"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
    
# number = random.randit(1, 10)
# print(number)

# import statistics 
# print((statistics.mean([100, 90]))
#       print (statistics)

# import sys
# print("Hellos, my name is", sys.argv[1])

# import statistics 
# import sys
# print(statistics.mean([int(sys.argv[1]), int(sys.argv[2])]))
      
      
import sys
import cowsay
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    # print("Too few arguments.")
    sys.exit()