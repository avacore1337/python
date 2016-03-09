
amount = int(input())

numbers = list(map(int, input().split()))

arrows = [0]*1000001
arr = 0
for x in numbers:
    if arrows[x] == 0:
        arr += 1
        arrows[x-1] += 1
    else:
        arrows[x] -= 1
        arrows[x-1] += 1
print(arr)
