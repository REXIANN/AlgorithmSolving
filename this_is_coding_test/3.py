# 3.문자열 뒤집기
import sys
sys.stdin = open("3input.txt", "r")
# 링크: https://www.acmicpc.net/problem/1439
N = input()
s = N[0]
count = 0
for n in N:
    if n != s:
        count += 1
        s = n
result = (count // 2 + 1) if count % 2 else (count //2)
print(result)