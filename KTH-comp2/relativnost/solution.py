import itertools

N, C = map(int, input().split())

colorPaintings = list(map(int, input().split()))
bwPaintings = list(map(int, input().split()))
amount = int(input())
for _ in range(amount):
    i, newColor, newBlack = map(int, input().split())
    i -= 1
    colorPaintings[i] = newColor
    bwPaintings[i] = newBlack
    for x in itertools.combinations([1, 2, 3, 1], 2):
        print(x[0]*x[1])
