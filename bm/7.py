def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    r, c = 0, 0
    dr = [ 1, -1]
    dc = [-1, 1]
    count = 0
    dir = 0 if horizontal else 1
    
    while not (r == n - 1 and c == n - 1):
        if horizontal:
            if c + 1 < n:
                c += 1
                horizontal = False
            else: 
                r += 1
        else:
            if r + 1 < n:
                r += 1
                horizontal = True
            else:
                c += 1
        count += 1
        answer[r][c] = count
        print(answer)
        
        while 0 <= r + dr[dir] < n and 0 <= c + dc[dir] < n:
            r += dr[dir]
            c += dc[dir]
            count += 2
            answer[r][c] = count
            print(answer)
        dir = 0 if dir else 1
    
    return answer

n, horizontal = 4, True
print(solution(n, horizontal))