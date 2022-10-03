students = list()
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        student = [name, score]
        students.append(student)
    students.sort(key = lambda x: x[1])
    second_stu = list()
    for student in students:
        if student[1] != students[0][1]:
            second_stu.append(student)
    second_least = sorted([sec[0] for sec in second_stu if sec[1] == second_stu[0][1]])
    for names in second_least:
        print(names)