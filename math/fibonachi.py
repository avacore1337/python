# http://tech-queries.blogspot.se/2010/09/nth-fibbonacci-number-in-ologn.html
# http://algorithmproblems.blogspot.se/2013/07/n-fibonacci-number-matrices.html

from numpy import *

def power(matrix, n):
    pass

def fibonacciNumber(n):
    matrix = matrix('1 1; 1 0')
    print(matrix)
    if n == 0:
        return 0
    

def main():
    n = input("what fibonacci number do you want?")
    print(fibonacciNumber(n))

if __name__ == '__main__':
    main()