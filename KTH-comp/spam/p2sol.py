from __future__ import division
from itertools import imap
minLength = int(raw_input())

numbers = list(imap(int, raw_input()))

theSum = 0
index = 0
length = minLength
for i in xrange(minLength, minLength*2 + 1):
    for j in xrange(len(numbers)-i + 1):
        tmpSum = 0
        for k in xrange(i):
            tmpSum += numbers[j+k]
        tmpSum = tmpSum/i
        if tmpSum > theSum:
            theSum = tmpSum
            index = j
            length = i

print index + 1, length
