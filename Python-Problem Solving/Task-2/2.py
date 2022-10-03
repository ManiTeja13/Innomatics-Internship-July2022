 n = int(raw_input())
 arr = map(int, raw_input().split())
 print(sorted(list(set(arr)))[-2])