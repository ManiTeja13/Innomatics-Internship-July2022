# Enter your code here. Read input from STDIN. Print output to STDOUT

N = input()
Grp_size = input().split()
Room_no_list = set(Grp_size)
for i in list(Room_no_list):
    Grp_size.remove(i)
Captain_Room_No = Room_no_list.difference(set(Grp_size)).pop()
print(Captain_Room_No)
