# 5162.py 두가지 빵의 딜레마
import sys
sys.stdin = open("5162input.txt", "r")

def backtrack(A, B, balance, count=0):
    if balance < 0: return
    max_count[0] = count if count > max_count[0] else max_count[0]
    backtrack(A, B, balance - A, count + 1)
    backtrack(A, B, balance - B, count + 1)


for tc in range(int(input())):
    A, B, C = map(int, input().split())
    max_count = [0]
    backtrack(A, B, C)
    print('#{} {}'.format(tc + 1, max_count[0]))