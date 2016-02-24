amount = int(input())

sum = 0
for i in range(3, amount):
    x = i - 1
    y = 0
    while x != 0:
        sum += x*y
        y += 1
        x -= 1
print(sum)
