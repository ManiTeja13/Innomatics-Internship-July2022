M = int(input())
mset = set(map(int, input().split()))

N = int(input())
nset = set(map(int, input().split()))

mdif = mset.difference(nset)
ndif = nset.difference(mset)

output = mdif.union(ndif)

for i in sorted(list(output)):
    print(i)