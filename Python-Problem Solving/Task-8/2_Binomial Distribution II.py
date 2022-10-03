# Refer: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def b(r, n, p):
    return nCr(n, r) * p**r * (1-p)**(n-r)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))