import random

moreThen20 = 0
for x in range(10000):  # lots of attemps
    # calculate the diff between the times
    thesum = 0
    for y in range(190):
        thesum += random.randint(0, 1)  # 1 for second, 0 for first
    thesum -= 95
    # check if more then 20 visited the first time
    if thesum >= 10:
        moreThen20 += 1

# percentage that has 20 or more difference
print(moreThen20/100)
