amount = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# print(numbers)
newList = []
i = 0
while i < amount - 2:
    if numbers[i]*2 + 3 == numbers[i+1] + numbers[i+2]:
        k = i+2
        while k < amount - 1 and numbers[k] + 1 == numbers[k+1]:
            k += 1
        newList.append(str(numbers[i])+"-"+str(numbers[k]))
        i = k+1
    else:
        newList.append(str(numbers[i]))
        i += 1
while i < amount:
    newList.append(str(numbers[i]))
    i += 1
print(" ".join(newList))
