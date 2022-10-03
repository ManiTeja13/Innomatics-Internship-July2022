# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

def mean(x):
    return round(sum(x)/(n),1)

def standardDeviation(values,mean):
    data=[(val-mean)**2 for val in values]
    return (sum(data)/(len(values)))**0.5


def pearsonCorrelationCoefficient(x,y):
    
    xMean=mean(x)
    yMean=mean(y)
    
    xStd=standardDeviation(x,xMean)
    yStd=standardDeviation(y,yMean)
    
    numerator = sum( (x[i]-xMean)*(y[i]-yMean) for i in range(n))
    denominator = n*xStd*yStd
    return round((numerator/denominator),3)

print (pearsonCorrelationCoefficient(x,y))

