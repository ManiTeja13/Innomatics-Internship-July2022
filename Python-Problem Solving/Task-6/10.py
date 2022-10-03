import numpy as np
n, m = list(map(int, input().split()))
a = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a, axis=None), 11))
