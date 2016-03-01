

def printList(data):
    print(" ".join(list(map(str, data))))


def printCase(case):
    print("Case #" + str(case + 1) + ":")


amount = int(input())

numbers = list(map(int, input().split()))

numbers = []
for i in range(4):
    numbers.append(list(map(int, input().split())))
