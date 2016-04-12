
def main():
    text = input()

    P, M = list(map(int, input().split()))

    for x in range(1000000):
        cop = text
        A = eval(cop)
        # print("A", A)
        if A % M == P:
            print(x)
            return
main()
