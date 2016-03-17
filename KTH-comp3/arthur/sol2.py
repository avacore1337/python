from __future__ import division
from itertools import imap

def printList(data):
    print u" ".join(list(imap(unicode, data)))


class Line(object):
    u"""docstring for Line"""
    def __init__(self, data, number):
        self.number = number + 1
        if data[0] < data[2]:
            self.x1 = data[0]
            self.y1 = data[1]
            self.x2 = data[2]
            self.y2 = data[3]
        else:
            self.x1 = data[2]
            self.y1 = data[3]
            self.x2 = data[0]
            self.y2 = data[1]

    def __gt__(self, other):
        # print(self.number, "vs", other.number)
        if self.x1 == other.x1:
            return self.y1 > other.y1
            # print(self.y1 > other.y1)
        if self.x1 > other.x1:
            return not other > self
        else:
            if self.x1 == self.x2:
                return False
            return (self.y2 - self.y1) / (self.x2 - self.x1) > (other.y1 - self.y1) / (other.x1 - self.x1)
            # print((self.y2 - self.y1) / (self.x2 - self.x1) > (other.y1 - self.y1) / (other.x1 - self.x1))


numbers = []
amount = int(raw_input())
for i in xrange(amount):
    numbers.append(Line(list(imap(int, raw_input().split())), i))

ans = []
tmp = numbers[0]
for i in xrange(amount - 1):
    for x in numbers:
        if tmp > x:
            tmp = x
    ans.append(tmp.number)
    numbers.remove(tmp)
    tmp = numbers[0]
ans.append(numbers[0].number)
printList(ans)
