
N, K, Q = map(int, input().split())
i = 2
c = 1
l = [1, 2]
if K == 1:
    for _ in range(Q):
        x, y = map(int, input().split())
        print(abs(x - y))
else:
    while i <= N:
        c *= K
        i += c
        l.append(i)
    le = len(l)

    # print(l)
    for _ in range(Q):
        # print("round:")
        x, y = map(int, input().split())
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
            x = x//K
            y = y//K
            dist += 2
        print(dist)
