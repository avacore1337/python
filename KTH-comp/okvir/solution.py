order = "#."


def fLine(length):
    global order
    ret = order*(length//2)
    if length % 2 == 1:
        ret += order[0]
    order = order[1] + order[0]
    return list(ret)

rows, columns = map(int, input().split())
U, L, R, D = map(int, input().split())
words = [input() for i in range(rows)]
# print(words)
output = []

for i in range(U + D + rows):
    output.append(fLine(columns + L + R))

for i in range(rows):
    for j in range(columns):
        output[i + U][j + L] = words[i][j]


for row in output:
    print("".join(row))
