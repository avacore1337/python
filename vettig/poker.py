import random

cards = [1]*26 + [-1]*27  # generate the cards, 1 for red -1 for rest

money = 0  # number of wins
for x in range(10000):
    rSum = 0
    guess = 0
    newCards = cards[:]
    random.shuffle(newCards)  # randomize the card order
    takeNext = False
    for card in newCards:
        if takeNext:
            money += card
            break
        if (rSum == -4):  # guess for the next if diff more then 4
            takeNext = True
        rSum += card
    if guess == 0:
        money += newCards[-1]  # default to last card if no guess
print(money)
