n = int(input())
s = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    s.remove(int(oper[1]))
  elif oper[0] == "discard":
    s.discard(int(oper[1]))
  else:
    s.pop()
    
print(sum(s))
