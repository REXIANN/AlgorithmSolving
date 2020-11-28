# 4522.py 세상의 모든 팰린드롬
import sys
sys.stdin = open("4522input.txt", "r")

for tc in range(int(input())):
    S = [i for i in input()]
    for i in range(len(S)//2):
        if S[i] == '?' or S[-(i + 1)] == '?':
            continue
        
        if S[i] != S[-(i + 1)]:
            print('#{} Not exist'.format(tc + 1))
            break
    else:
        print('#{} Exist'.format(tc + 1))