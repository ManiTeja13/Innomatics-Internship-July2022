Result =[]
markslist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        marks = float(input())
        Result+=[[name,marks]]
        markslist+=[marks]
    b=sorted(list(set(markslist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)