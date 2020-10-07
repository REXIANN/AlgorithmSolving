# 1006.py 습격자 초라기
import sys
sys.stdin = open("1006input.txt", "r")

dr = [0, 1, 0]
dc = [-1, 0, 1]
def backtrack(k, N, W, count):
    if count > minV[0]: return

    row, col = k // N, k % N # k 로부터 행과 열을 뽑아냄
    
    if k == (N * 2):
        minV[0] = count if count < minV[0] else minV[0]
        count = 0
    elif visited[row][col]:
        backtrack(k + 1, N, W, count)
    else:
        visited[row][col] = True # 해당위치 방문마킹
        count += 1 # 해당칸 점령했으니 +1
        soldier = W - circle[row][col] # 남은 병사 수
        flag = 1
        for i in range(3):
            row_in = abs(row - dr[i])
            col_in = N -1 if col + dc[i] < 0 else (col + dc[i]) % N
            if soldier >= circle[row_in][col_in] and not visited[row_in][col_in]:
                visited[row_in][col_in] = True
                backtrack(k + 1, N, W, count)
                visited[row_in][col_in] = False
                flag = 0
        if flag == 1: 
            backtrack(k + 1, N, W, count)
            flag = 0
        visited[row][col] = False
    

for tc in range(int(input())):
    N, W = map(int, input().split())
    circle = []
    for _ in range(2):
        circle.append(list(map(int, input().split())))
    visited = [[False] * N, [False] * N]
    minV = [N * 2] 
    backtrack(0, N, W, 0)
    print(minV[0])