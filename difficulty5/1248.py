# 1248.py 공통조상
import sys
sys.stdin = open("1248input.txt", "r")
# 인접행렬풀이 - 시간초과 뜸
def find_parent(k):
    stack = [k]
    while stack:
        kk = stack.pop()
        for i in range(V + 1):
            if matrix[i][kk]:
                if parent_node[i]:
                    return i
                else:
                    parent_node[i] += 1
                    stack.append(i)


def find_child(k):
    count = 1
    stack = [k]
    while stack:
        kk = stack.pop()
        for i in range(V + 1):
            if matrix[kk][i]:
                stack.append(i)
                count += 1
    return count


for tc in range(int(input())):
    V, E, X, Y = map(int, input().split())
    L = list(map(int, input().split()))
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(0, len(L), 2):
        matrix[L[i]][L[i + 1]] = 1
    parent_node = [0] * (V + 1)
    find_parent(X)
    parent = find_parent(Y)
    children = find_child(parent)
    print('#{} {} {}'.format(tc + 1, parent, children))
