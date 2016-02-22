a = [0]*10
for i in range(1, 10000):
    a[int(str(2**i)[0])] += 1

for i, value in enumerate(a):
    print(i, " ", a[i])
