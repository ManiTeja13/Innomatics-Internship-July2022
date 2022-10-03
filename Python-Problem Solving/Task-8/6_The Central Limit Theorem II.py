# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

tickets=float(input())
n=float(input())
mean=float(input())
sd=float(input())

def centralLimitTheorem(tickets,n,mean,sd):
    newMean=n*mean
    newSd=(n**0.5)*sd     
    return round(0.5 * (1 + math.erf((tickets - newMean) / (newSd * (2 ** 0.5)))),4)

print (centralLimitTheorem(tickets,n,mean,sd))
