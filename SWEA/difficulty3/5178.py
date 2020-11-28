# 5178.py 노드의 합
import sys
sys.stdin = open("5178input.txt", "r")

def binary_tree(L, tree):
    if L > (len(tree) - 1): return 0
    return tree[L] if tree[L] != 0 else binary_tree(L * 2, tree) + binary_tree(L * 2 + 1, tree)
    

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        tree[x] = y
    result = binary_tree(L, tree)
    print('#{} {}'.format(tc + 1, result))