def solution(n):
    answer = 0
    memo = [2]
    for i in range(2, n + 1):
        for m in memo:
            if i % m == 0:
                break
        else:
            memo.append(i)
                
    print(memo)
    return answer

solution(1000000)



