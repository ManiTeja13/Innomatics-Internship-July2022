'''Refer:https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem '''


# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))


def b(r, n, p):
    return nCr(n, r) * p**r * (1-p)**(n-r)

l, r = list(map(float, input().split(" ")))
odds = l / r
print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))