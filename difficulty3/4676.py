# 4676.py 늘어지는 소리 만들기
import sys
sys.stdin = open("4676input.txt", "r")

for tc in range(int(input())):
    string, H = input(), input()
    M = [0] * (len(string) + 1)
    for i in map(int, input().split()): M[i] += 1
    for i in range(len(string), -1, -1):
        if not M[i] : continue
        string = string[:i] + "-" * M[i] + string[i:]
    print('#{} {}'.format(tc+1, string))