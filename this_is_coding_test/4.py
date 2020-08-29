# 4.만들 수 없는 금액
import sys
sys.stdin = open('4input.txt', 'r')
N = int(input())
L = list(sorted(list(map(int, input().split())))) 
S = list(set(L))
max_v = sum(L)
T = [0] * (max_v + 1)
for s in S:
    T[s] = 1

for l in L:
    print(T)
    for idx, val in enumerate(T):
        if val == 1 and (idx + l) < len(T):
            
            if T[idx + l] != 1:
                T[idx + l] = 1
print(T)