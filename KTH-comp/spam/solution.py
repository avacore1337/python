minLength = int(input())

numbers = list(map(int, input()))

theSum = 0
index = 0
length = minLength
for i in range(minLength, minLength*2 + 1):
    for j in range(len(numbers)-i + 1):
        tmpSum = 0
        for k in range(i):
            tmpSum += numbers[j+k]
        tmpSum = tmpSum/i
        if tmpSum > theSum:
            theSum = tmpSum
            index = j
            length = i

print(index + 1, length)
