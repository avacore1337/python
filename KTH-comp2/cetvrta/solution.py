

def printList(data):
    print(" ".join(list(map(str, data))))


def printCase(case):
    print("Case #" + str(case + 1) + ":")


first = []
second = []
for x in range(3):
    numbers = list(map(int, input().split()))
    first.append(numbers[0])
    second.append(numbers[1])
first.sort()
second.sort()

if first[0] == first[1]:
    print(first[2], end=" ")
else:
    print(first[0], end=" ")

if second[0] == second[1]:
    print(second[2])
else:
    print(second[0])
