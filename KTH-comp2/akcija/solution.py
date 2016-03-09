amount = int(input())
numbers = []
for i in range(amount):
    numbers.append(int(input()))
numbers.sort()
theSum = 0
# print(numbers)
for i in range(0, len(numbers)//3):
    theSum += numbers[-i*3 - 1]
    # print(numbers[-i*3 - 1])
    theSum += numbers[-i*3 - 2]
    # print(-i*3 - 2)
for x in numbers[0:(len(numbers) % 3)]:
    theSum += x
print(theSum)
