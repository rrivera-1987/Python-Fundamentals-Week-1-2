import random

pips = random.randint(1, 6)
print("You roll the dice... it lands with",pips, "pips showing")

prizes = ["a car", "$1,000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("You turn the wheel of fortune... it lands on a prize of",prize_won + "!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("The cars are now in this order: ")
print(cards)