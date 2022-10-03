if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    out=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                    out.append([i,j,k])
    print(out)




By using list comprehension

x=int(input())
y=int(input())
z=int(input())
n=int(input())

lst_comp=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
print(lst_comp)