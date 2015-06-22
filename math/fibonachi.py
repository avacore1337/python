# http://tech-queries.blogspot.se/2010/09/nth-fibbonacci-number-in-ologn.html
# http://algorithmproblems.blogspot.se/2013/07/n-fibonacci-number-matrices.html

# from numpy import *
import math

def multiply2x2(m1, m2):
    response = [[0,0],[0,0]]
    response[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0];
    response[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1];
    response[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0];
    response[1][1] = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1];
    return response

def power(m, n):
    print(n)
    if n == 1:
        return m
    r = power(m, math.floor(n/2))
    r = multiply2x2(r,r)
    if n%2 == 1:
        r = multiply2x2(r,m)
    return r

def fibonacciNumber(n):
    m = [[1, 1], [1, 0]]
    print(m)
    if n == 0:
        return 0
    r = power(m, n - 1)
    return r[0][0]

def main():
    n = int(input("what fibonacci number do you want?"))
    print(fibonacciNumber(n))

if __name__ == '__main__':
    main()