import random
import math


def isFull(phils):  # check if gotten all philosophers
    for phil in phils:
        if not phil:
            return False
    return True


def fullset(size):
    print("n*e is ", size*math.e)
    print("n*log(n) is ", size*math.log(size))
    phils = [False]*size
    count = 0
    while not isFull(phils):  # draw new until you have all
        count += 1
        phils[random.randint(0, size - 1)] = True  # draw a random
    print("actual value is: ", count)

fullset(1000)
