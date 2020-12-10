def solution(board, moves):
    # 행렬을 뒤집어서 각 열이 하나의 리스트가 되도록 만듬
    N = len(board[0])
    new_board = [[0] *N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            new_board[j][N-(1 + i)] = board[i][j]
    
    # 값이 0인 녀석들을 제거해서 pop하기 쉽게 만들어 놓음
    for i in range(N):
        while True:
            a = new_board[i].pop()
            if a == 0:
                continue
            else:
                new_board[i].append(a)
                break
    
    # 인형뽑기 시작
    answer = 0
    stack = []
    for move in moves:
        move -= 1
        if len(new_board[move]) > 0:
            muji = new_board[move].pop()
        else:
            continue
            
        if len(stack) == 0:
            stack.append(muji)
        else:
            leo = stack.pop()
            
            if leo == muji:
                answer += 2
                continue
            else: 
                stack.append(leo)
                stack.append(muji)
                
    return answer