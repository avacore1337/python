import itertools


def printData(data, questions):
    for i in range(questions - 1, -1, -1):
        print(data // (1 << (i)), end="")
        data = data % (1 << (i))
        # print("data: ", 1 << i)
    print()


def countOnes(number):
    count = 0
    while number > 0:
        count += 1
        number &= number - 1
    return count


def solveTest():
    students, questions = map(int, input().split())
    # print(students, questions)
    data = []
    inverse = (1 << questions) - 1
    # print("invers: ", inverse)
    for i in range(students):
        answers, correct = input().split()
        correct = int(correct)
        answers = answers[::-1]
        aSum = 0
        for i in range(questions):
            if answers[i] == '1':
                aSum += 1 << i
        if correct < questions//2:
            aSum = inverse - aSum
            correct = questions - correct
        data.append((correct, aSum))
    data.sort()
    maxScore = data[-1][0]
    maxGuess = data[-1][1]
    bits = [1 << i for i in range(questions)]
    correctAns = []
    # if maxScore < questions:
    for permutation in itertools.combinations(bits, maxScore):
        theVal = sum(permutation)
        theVal ^= maxGuess
        fail = False
        for value in data:
            count = countOnes(theVal ^ value[1])
            if(count != value[0]):
                fail = True
                break
        if not fail:
            correctAns.append(theVal)
        # print("theval: ", bin(theVal))
    if len(correctAns) == 1:
        printData(inverse - correctAns[0], questions)
    else:
        print(str(len(correctAns)) + " solutions")
    # else:
    #     # print("maxguess")
    #     printData(maxGuess, questions)

    # print(bits)
    # print(data)

rounds = int(input())
for round in range(rounds):
    solveTest()
