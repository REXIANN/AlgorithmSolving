# 3378.py 스타일리쉬 들여쓰기
import sys
sys.stdin = open("3378input.txt", "r")
codes = '(){}[]'
index = [0, 0, 0, 0, 0, 0]
def count_dot(phrase):
    for i in range(len(phrase)):
        if phrase[i] != '.': return i


for tc in range(int(input())):
    p, q = map(int, input().split())
    P = [input() for _ in range(p)]
    Q = [input() for _ in range(q)]
    results = [0] * len(P)
    # print(p, q)
    # print(P, '\n', Q)
    # result = R(a - b) + C(c - d) + S(e - f)
    for i in range(len(P)):
        results[i] = count_dot(P[i])
        for char in P[i]:
            if char in codes:
                index[codes.index(char)] += 1
        print(results)
        print(index)