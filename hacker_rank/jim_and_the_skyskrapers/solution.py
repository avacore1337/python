from collections import deque


def trinum(num):
    return int((num * (num-1))/2)


def main():
    numbers = deque()
    input()
    buildings = list(map(int, input().split()))
    total = 0
    for building in buildings:
        try:
            top = numbers.pop()
            while top[0] < building:
                total += trinum(top[1])
                top = numbers.pop()
            if top[0] == building:
                top[1] += 1
                numbers.append(top)
            else:
                numbers.append(top)
                numbers.append([building, 1])
        except IndexError:
            numbers.append([building, 1])
    for num in numbers:
        total += trinum(num[1])
    print(total*2)


main()
