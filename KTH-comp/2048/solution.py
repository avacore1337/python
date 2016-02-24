def rotate90(matrix):
    return [list(x) for x in list(zip(*matrix[::-1]))]


numbers = []
for i in range(4):
    numbers.append(list(map(int, input().split())))
rotate = int(input())
if rotate % 2 == 1:
    rotate = (rotate + 2) % 4
for i in range(rotate):
    numbers = rotate90(numbers)

# for row in numbers:
#     print(row)

for i in range(4):
    row = numbers[i]
    for j in range(3):
        count = 0
        while row[j] == 0 and count < 4:
            for k in range(j, 3):
                row[k] = row[k+1]
            row[3] = 0
            count += 1
    # print()
    # print(row)
    # print()
    if row[0] == row[1]:
        if row[2] == row[3]:
            # print("two pairs")
            # print(row)
            row[0] = row[0]*2
            row[1] = row[2]*2
            row[2] = 0
            row[3] = 0
        else:
            # print("01-pair")
            # print(row)
            row[0] = row[0]*2
            row[1] = row[2]
            row[2] = row[3]
            row[3] = 0
    elif row[1] == row[2]:
        # print("12-pair")
        # print(row)
        row[1] = row[1]*2
        row[2] = row[3]
        row[3] = 0
    elif row[2] == row[3]:
        # print("23-pair")
        # print(row)
        row[2] = row[2]*2
        row[3] = 0


for i in range((4 - rotate) % 4):
    numbers = rotate90(numbers)

for row in numbers:
    print(" ".join(list(map(str, row))))
