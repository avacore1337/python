import random

# The total amount of boys and girls
boygirls = []
for x in range(10000):  # lots of attempts
    val = random.randint(0, 1)  # one for boy zero for girl
    boygirls.append(val)
    while val != 1:
        val = random.randint(0, 1)
        boygirls.append(val)

print(sum(boygirls)/len(boygirls))  # The quote of boys vs girls
