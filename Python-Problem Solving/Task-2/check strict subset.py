set1= set(input().split())
N = int(input())
output = True

for i in range(N):
    set2 = set(input().split())
    if not set2.issubset(set1):
        output = False
    if len(set2) >= len(set1):
        output = False

print(output)