N1 = int(input())
set1 = set(input().split());

N2 = int(input())
set2 = set(input().split());

diff_set = set1.difference(set2)

print(len(diff_set))
