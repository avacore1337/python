import math
_, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
numLen = len(numbers)
su = 0

if K > 1:
    numbers = numbers[:-(K - 1)]
for i, x in enumerate(numbers):
    # print(x)
    val = 1
    for j in range(K - 1):
        val *= numLen - 1 - j - i
    val = val//math.factorial(K - 1)
    # print("val", val)
    su += x*val
    # print("total", x*val)
print(su)
