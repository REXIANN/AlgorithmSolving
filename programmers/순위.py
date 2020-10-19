def solution(n, results):
    score = [[0 for __ in range(n)]  for _ in range(n)]
    winners = [[0 for __ in range(n)]  for _ in range(n)]
    losers = [[0 for __ in range(n)]  for _ in range(n)]
    check = [0 for _ in range(n)]
    INF = 99999
    for result in results:
        w, l = result[0] - 1, result[1] - 1
        score[l][w] = 1
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if not score[i][j]:
                winners[i][j] = INF
            else:
                winners[i][j] = score[i][j]
    
    for i in range(n):
        check[i] = sum(score[i])
    
    
    for _ in range(n):
        print(winners[_])
    print()
    print(check)

    count = 0
    # for i in range(n):
    #     value = sum(winners[i])
    #     for j in range(n):
    #         if winners[i][j] != 0:
    #             value += check[j]        
    #     if value == n - 1:
    #         count += 1
    
    return count


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))