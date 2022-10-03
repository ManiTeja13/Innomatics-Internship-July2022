# Enter your code here. Read input from STDIN. Print output to STDOUT
Eng_stud=int(input())
Eng_stud_roln=set(input().split())

Fren_stud=int(input())
Fren_stud_roln=set(input().split())

symm_diff_set=Eng_stud_roln.intersection(Fren_stud_roln)

print(len(symm_diff_set))