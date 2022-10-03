# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

m = 9800
n = 49
mean = n * 205
std = (n ** 0.5) * 15


cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * ( 2 ** 0.5))))

print(cdf(m))