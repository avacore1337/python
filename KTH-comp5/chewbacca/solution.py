
N, K, Q = map(int, input().split())

if K == 1:
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(x - y))
else:
    for _ in range(Q):
        x, y = map(int, input().split())
        dist = 0


        # print("x:", x)
        xlen = -1
        for i in l:
            if x < i:
                break
            # print("i:", i)
            xlen += 1
        # print("xlen:", xlen)
        ylen = -1
        for i in l:
            if y < i:
                break
            # print("i:", i)
            ylen += 1
        # print("ylen:", ylen)
        x -= l[xlen]
        y -= l[ylen]
        # print("x: ", x)
        # print("y: ", y)
        dist = 0
        while xlen != ylen:
            if xlen > ylen:
                dist += 1
                xlen -= 1
                x = x//K
            elif xlen < ylen:
                dist += 1
                ylen -= 1
                y = y//K
        # print("dist:", dist)
        while x != y:
            x = x//3
            y = y//3
            dist += 2
        print(dist)
