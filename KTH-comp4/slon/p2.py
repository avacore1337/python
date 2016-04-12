from itertools import imap

def main():
    text = raw_input()

    P, M = list(imap(int, raw_input().split()))

    for x in xrange(100000):
        cop = text
        A = eval(cop)
        # print("A", A)
        if A % M == P:
            print x
            return
main()
