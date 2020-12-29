from collections import deque

def solution(n, results):
    matrix = [[0] * n for _ in range(n)]
    count = 0
    for result in results:
        win, lose = result[0] - 1, result[1] - 1
        matrix[lose][win] = 1
    
    # for i in range(n):
    #     print(matrix[i])
    # print()

    for i in range(n):
        inner_count = 0
        # if i is winner
        visited = set([i])
        dq = deque([i])
        while dq:
            player = dq.popleft()
            for j in range(n):
                if matrix[player][j] == 1 and not j in visited:
                    visited.add(j)
                    inner_count += 1
                    dq.append(j)
        # print(i, 'win', inner_count)
        
        # if i is loser
        visited = set([i])
        dq = deque([i])
        while dq:
            player = dq.popleft()
            for j in range(n):
                if matrix[j][player] == 1 and not j in visited:
                    visited.add(j)
                    inner_count += 1
                    dq.append(j)
        # print(i, 'lose', inner_count)
        if inner_count >= n - 1:
            count += 1
    return count


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))