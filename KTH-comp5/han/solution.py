

def printList(data):
    print(" ".join(list(map(str, data))))


def printCase(case):
    print("Case #" + str(case + 1) + ":")

lett = [0]*27
amount = int(input())
o = 1
for i in range(amount):
    order = input().split()
    if order[0] == "UPIT":
        a = int(order[1])
        c = ord(order[2])-97
        print(a, c)
    else:
        rev = int(order[1])
        print(rev)
