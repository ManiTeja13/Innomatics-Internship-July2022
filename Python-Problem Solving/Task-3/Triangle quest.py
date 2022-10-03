'''
1
22
333
4444
55555
......
'''


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(i*10**i/9))