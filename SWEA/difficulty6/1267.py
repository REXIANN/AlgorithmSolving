# 1267.py 작업순서
import pprint
import sys
sys.stdin = open("1267input.txt", "r")


for test_count in range(1, 11):
    print('#{}'.format(test_count), end=" ")
    V_, E_ = tuple(map(int, input().split()))
    trunks = list(map(int, input().split()))
    graph = [[0 for _ in range(V_)] for _ in range(V_)]
    visit_ = [0 for _ in range(V_)]
    stack = []
    result = []

    for i in range(0, len(trunks), 2):
        graph[trunks[i] - 1][trunks[i + 1] - 1] = 1
    
    for i in range(V_):
        count = 0
        for j in range(V_):
            count += graph[j][i]
        if count == 0:
            stack.append(i)
        else:
            visit_[i] = count

    while stack:
        v = stack.pop(-1)
        if visit_[v] == 0:
            visit_[v] = 1
            result.append(str(v + 1))
        for i in range(V_):
            if graph[v][i] == 1:
                visit_[i] -= 1
                if visit_[i] == 0:
                    stack.append(i)

    print(' '.join(result))



