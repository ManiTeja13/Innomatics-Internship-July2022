# Enter your code here. Read input from STDIN. Print output to STDOUT
len_set = int(input())
set_A = set(map(int, input().split()))
other_sets = int(input())
for i in range(other_sets):
    oper = input().split()
    if oper[0] == 'intersection_update':
        set_N = set(map(int, input().split()))
        set_A.intersection_update(set_N)
    elif oper[0] == 'update':
        set_N = set(map(int, input().split()))
        set_A.update(set_N)
    elif oper[0] == 'symmetric_difference_update':
        set_N = set(map(int, input().split()))
        set_A.symmetric_difference_update(set_N)
    elif oper[0] == 'difference_update':
        set_N = set(map(int, input().split()))
        set_A.difference_update(set_N)
    else :
        print('Invalid operation)
print(sum(set_A))