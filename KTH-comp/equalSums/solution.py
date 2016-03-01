import itertools


def getDisjoint(theSet, sets):
    for i in range(len(sets)):
        success = True
        for x in theSet:
            if x in sets[i]:
                success = False
                break
        if success:
            return sets[i]
    return None


def printList(data):
    print(" ".join(list(map(str, data))))


def findDisjointSets(round):
    print("Case #" + str(round + 1) + ":")
    sums = {}
    numbers = list(map(int, input().split()))
    numbers = numbers[1:]
    for j in range(len(numbers)):
        for theSet in itertools.combinations(numbers, j):
            theSum = sum(theSet)
            if theSum in sums:
                sets = sums[theSum]
                for i in range(len(sets)):
                    disjoint = getDisjoint(theSet, sets)
                    if(disjoint):
                        printList(theSet)
                        printList(disjoint)
                        return
                sets.append(theSet)
            else:
                sums[theSum] = [theSet]
    print("Impossible")
    for key in sums.keys():
        if len(sums[key]) > 1:
            print(len(sums[key]))


rounds = int(input())

for i in range(rounds):
    findDisjointSets(i)
