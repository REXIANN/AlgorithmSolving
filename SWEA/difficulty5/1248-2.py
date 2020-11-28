# 1248.py 공통조상
import sys
sys.stdin = open("1248input.txt", "r")

def find_parent(k):
    stack = [k]
    while stack:
        kk = stack.pop()
        for i in range(V + 1):
            if kk in matrix[i]:
                if not parent_node[i]:
                    stack.append(i)
                    parent_node[i] += 1
                else:
                    return i


def find_child(k):
    count = 1
    stack = [k]
    while stack:
        kk = stack.pop()
        for i in matrix[kk]:
            stack.append(i)
            count += 1
    return count


for tc in range(int(input())):
    V, E, X, Y = map(int, input().split())
    L = list(map(int, input().split()))
    matrix = [[] for _ in range(V + 1)]
    for i in range(0, len(L), 2):
        matrix[L[i]].append(L[i + 1])
    parent_node = [0] * (V + 1)
    find_parent(X)
    parent = find_parent(Y)
    children = find_child(parent)
    print('#{} {} {}'.format(tc + 1, parent, children))
