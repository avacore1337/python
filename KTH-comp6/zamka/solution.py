def main():

    mi = int(input())
    ma = int(input())
    su = int(input())

    for i in range(mi, ma + 1):
        if sum(map(int, list(str(i)))) == su:
            print(i)
            break
    for i in range(ma, mi - 1, -1):
        if sum(map(int, list(str(i)))) == su:
            print(i)
            break
main()
