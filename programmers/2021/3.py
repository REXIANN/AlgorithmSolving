def solution(info, query):
    infos = [( set(inf.split()[:4]), int(inf.split()[4])) for inf in info]
    answer = []
    for quer in query:
        quer = quer.split()
        score = int(quer.pop())
        sub_q = set(q for q in quer if q != '-' and q != 'and')
        count = 0

        for inf in infos:
            if score <= inf[1] and sub_q.issubset(inf[0]):
                count += 1
        answer.append(count)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
