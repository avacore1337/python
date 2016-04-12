

def printList(data):
    print(" ".join(list(map(str, data))))

ans = []
amount = int(input())
for i in range(amount):
    numbers = list(map(int, input().split()))
    y = 0
    for x in numbers:
        y = y | x
    ans.append(y)
printList(ans)
