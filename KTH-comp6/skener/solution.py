
r, c, rMul, cMul = map(int, input().split())

for i in range(r):
    row = list(input())
    newRow = ""
    for c in row:
        newRow += c*cMul
    for j in range(rMul):
        print(newRow)
