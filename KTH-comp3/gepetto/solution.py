
def recSum(start, end):
    ret = 1
    for i in range(start + 1, end):
        v = (start, i)
        if v not in numbers:
            ret += recSum(i, end)
    return ret

topings, restrictions = map(int, input().split())

numbers = set()
for i in range(restrictions):
    x = list(map(int, input().split()))
    x.sort()
    x = tuple(x)
    # print(x)
    numbers.add(x)
# print(list(numbers))
print(recSum(0,topings + 1))
