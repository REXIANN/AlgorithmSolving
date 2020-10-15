def solution(k, score):
    diff = [score[i] - score[i + 1] for i in range(len(score) - 1)]

    diff_dict = {}

    for dif in diff:
        if diff_dict.get(dif):
            diff_dict[dif] += 1
        else:
            diff_dict[dif] = 1
    print(diff_dict)

    arr = set(key for key, value in diff_dict.items() if value >= k)
    
    print(arr)
    result = [True if dif in arr else False for dif in diff]
    print(result)
    
    count = 0
    flag = False
    for elem in result:
        if elem:
            count += 1
            flag = True
        
        if not elem and flag:
            count += 1
            flag = False
    if flag:
        count += 1
    print(count, len(score) - count)
    
    
    return 0


k = 3
score = [24, 22, 20, 10, 5, 3, 2, 1]
print(solution(k, score))