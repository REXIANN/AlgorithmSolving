# 4871.py 그래프 경로
import pprint
import sys
sys.stdin = open("4871input.txt", "r")
tc = int(input())

for test_count in range(1, tc + 1):
    V_, E_ = tuple(map(int, input().split()))
    graph = [[0 for _ in range(V_)] for _ in range(V_)]
    for _ in range(E_):
        x_, y_ = tuple(map(int, input().split()))
        graph[x_ - 1][y_ - 1] = 1
    S_, G_ = tuple(map(int, input().split()))
    flag = 0

    stack = []
    visit = [False for _ in range(V_)]
    stack.append(S_ - 1)
    while len(stack) > 0:
        i = stack.pop(-1)
        if i == G_ - 1:
            flag = 1
            break

        if visit[i] == False:
            visit[i] = True
            stack.append(i)

        for j in range(V_):
            if graph[i][j] == 1 and visit[j] == False:
                stack.append(j)
    print('#{} {}'.format(test_count, flag))