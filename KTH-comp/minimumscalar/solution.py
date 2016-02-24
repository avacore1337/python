cases = int(input())

for i in range(cases):
    length = int(input())
    ys = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ys.sort()
    xs.sort()
    xs = xs[::-1]
    sum = 0
    for j in range(length):
        sum += ys[j]*xs[j]
    print("Case #" + str(i + 1) + ": " + str(sum))
