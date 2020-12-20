def solution(answers):
    k = '1345'
    j = '31245'
    L = len(answers)
    answer1 = [(i % 5) + 1 for i in range(L)]
    answer2 = []
    answer3 = []
    # answer2
    idx = 0
    answer2_append = answer2.append
    for i in range(L):
        if not i % 2:
            answer2_append('2')
        else:
            answer2_append(k[idx])
            idx = (idx + 1) % 4
    answer2 = list(map(int, answer2))
    
    # answer3
    idx, count = 0, 0
    answer3_append = answer3.append
    for i in range(L):
        answer3_append(j[idx])
        count += 1
        if count == 2:
            idx = (idx + 1) % 5
            count = 0
    answer3 = list(map(int, answer3))
    
    # result1
    result1 = 0
    for i in range(L):
        if answers[i] == answer1[i]:
            result1 += 1
    # result2
    result2 = 0
    for i in range(L):
        if answers[i] == answer2[i]:
            result2 += 1
    # result3
    result3 = 0
    for i in range(L):
        if answers[i] == answer3[i]:
            result3 += 1
    
    if result1 > result2:
        if result1 > result3:
            answer = [1]
        elif result1 == result3:
            answer = [1, 3]
        else:
            answer = [3]
    elif result1 == result2:
        if result1 > result3:
            answer = [1, 2]
        elif result1 == result3:
            answer = [1, 2, 3]
        else:
            answer = [3]
    else:
        if result2 > result3:
            answer = [2]
        elif result2 == result3:
            answer = [2, 3]
        else:
            answer = [3]
    return answer