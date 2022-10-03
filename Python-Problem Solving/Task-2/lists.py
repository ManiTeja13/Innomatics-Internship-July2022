if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        c=input().split()
        cmd=c[0]
        
        
        if cmd=="insert":
            l.insert(int(c[1]),int(c[2]))
        if cmd=="print":
            print(l)
        if cmd=="remove":
            l.remove(int(c[1]))
        if cmd=="sort":
            l.sort()
        if cmd=="pop":
            l.pop()
        if cmd=="append":
            l.append(int(c[1]))
        if cmd=="reverse":
            l.reverse()