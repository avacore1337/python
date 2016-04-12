
amount = int(input())

inGoing = [0]*(amount + 1)
outGoing = [0]*(amount + 1)
for value in range(amount - 1):
    f, t = map(int, input().split())
    if linkCount[f] == 0:
        print(1)
        linkCount[t] += 1
    else:
        print(0)
        linkCount[f] += 1
