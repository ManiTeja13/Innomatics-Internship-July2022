# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn import linear_model

lst = list(map(int, str.split(input(), " ")))
m, n = lst[0], lst[1]
data = [list(float(x) for x in input().split()) for i in range(n)]

x = [[item[i] for i in range(m)] for item in data]
y = [item[-1] for item in data]

lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

for i in range(int(input())):
    data = list(map(float, input().split()))
    ans = [b[j]*data[j] for j in range(m)]
    print(a+sum(ans))