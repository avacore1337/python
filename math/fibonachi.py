# http://tech-queries.blogspot.se/2010/09/nth-fibbonacci-number-in-ologn.html
# http://algorithmproblems.blogspot.se/2013/07/n-fibonacci-number-matrices.html

from numpy import *

def power(m, n):
    print(n)
    if n == 1:
        return m
    r = power(m, math.floor(n/2))
    r = r*r
    if n%2 == 1:
        r = r*m
    return r

def fibonacciNumber(n):
    m = matrix('1 1; 1 0')
    print(m)
    if n == 0:
        return 0
    r = power(m, n - 1)
    return r.A[0][0]

def main():
    n = int(input("what fibonacci number do you want?"))
    print(fibonacciNumber(n))

if __name__ == '__main__':
    main()