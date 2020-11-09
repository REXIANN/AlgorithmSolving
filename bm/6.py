def solution(logs):
    # 수험번호, 문제번호, 받은점수 순서
    students = dict()
    cheaters = set()
    ids = []
    # create students dict
    for log in logs:
        log = list(log.split())
        id = log[0]
        if students.get(id):
            for i in range(len(students[id][0])):
                if students[id][0][i] == log[1]:
                    students[id][1][i] = log[2]
                    break
            else:
                students[id][0].append(log[1])
                students[id][1].append(log[2])
        else:
            students[id] = [[log[1]], [log[2]]]
            ids.append(id)

    # evaluate 
    for i in range(len(ids) - 1):
        student1 = students[ids[i]]
        for j in range(i + 1, len(ids)):
            student2 = students[ids[j]]
            if len(student1[0]) < 5 or len(student2[0]) < 5:
                continue
            if set(student1[0]) == set(student2[0]):
                for k, v in enumerate(student1[0]):
                    score1 = student1[1][k]
                    idx2 = student2[0].index(v)
                    score2 = student2[1][idx2]
                    if score1 != score2:
                         break
                    # print(score1, score2)
                else: 
                    cheaters.add(ids[i])
                    cheaters.add(ids[j])        

    cheaters = list(sorted(cheaters))

    return cheaters if cheaters else ['None']

logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]
logs = ["1901 10 50", "1909 10 50"]
print(solution(logs))