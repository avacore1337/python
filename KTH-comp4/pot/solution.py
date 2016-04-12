
amount = int(input())
theSum = 0

for i in range(amount):
    text = input()
    theSum += int(text[:-1])**int(text[-1])

print(theSum)
