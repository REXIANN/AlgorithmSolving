# 5174.py subtree
import sys
sys.stdin = open("5174input.txt", "r")

for tc in range(int(input())):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E + 2)]
    EE = list(map(int, input().split()))
    for i in range(0, len(EE), 2):
        idx = EE[i]
        value = EE[i + 1]
        tree[idx].append(value)
    # print(tree)
    
    stack = [elem for elem in tree[N]]
    count = 1
    while stack:
        elem = stack.pop()
        count += 1
        while tree[elem]:
            element = tree[elem].pop()
            stack.append(element)
    print('#{} {}'.format(tc + 1, count))    
