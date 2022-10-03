# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    x= input()
    a=set(input().split())
    z=input()
    b=set(input().split())
    print(a.issubset(b))