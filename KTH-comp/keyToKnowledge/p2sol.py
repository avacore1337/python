from __future__ import absolute_import
import itertools
import sys
from itertools import imap


def printData(data, questions):
    for i in xrange(questions - 1, -1, -1):
        print data // (1 << (i)),; sys.stdout.write(u"")
        data = data % (1 << (i))
        # print("data: ", 1 << i)
    print


def countOnes(number):
    count = 0
    while number > 0:
        count += 1
        number &= number - 1
    return count


def solveTest():
    students, questions = imap(int, raw_input().split())
    # print(students, questions)
    data = []
    inverse = (1 << questions) - 1
    # print("invers: ", inverse)
    for i in xrange(students):
        answers, correct = raw_input().split()
        correct = int(correct)
        answers = answers[::-1]
        aSum = 0
        for i in xrange(questions):
            if answers[i] == u'1':
                aSum += 1 << i
        if correct < questions//2:
            aSum = inverse - aSum
            correct = questions - correct
        data.append((correct, aSum))
    data.sort()
    maxScore = data[-1][0]
    maxGuess = data[-1][1]
    bits = [1 << i for i in xrange(questions)]
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
        print unicode(len(correctAns)) + u" solutions"
    # else:
    #     # print("maxguess")
    #     printData(maxGuess, questions)

    # print(bits)
    # print(data)

rounds = int(raw_input())
for round in xrange(rounds):
    solveTest()
