ball = 1

for x in input():
    if x == "A" and ball == 1:
        ball = 2
    elif x == "A" and ball == 2:
        ball = 1
    elif x == "B" and ball == 3:
        ball = 2
    elif x == "B" and ball == 2:
        ball = 3
    elif x == "C" and ball == 1:
        ball = 3
    elif x == "C" and ball == 3:
        ball = 1
print(ball)
