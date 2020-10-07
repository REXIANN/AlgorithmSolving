# 5948.py 새샘이의 7-3-5 게임
import sys
sys.stdin = open("5948input.txt", "r")

def combination(k, N, start_num, s=0):
    if k == N:
        result.add(s)
    else:
        for i in range(start_num, len(num_list) + k + 1 -3):
            combination(k + 1, N, i + 1, s + num_list[i])


for tc in range(int(input())):
    num_list = list(map(int, input().split()))
    result = set()
    combination(0, 3, 0)
    result = list(sorted(result, reverse=True))[4]
    print('#{} {}'.format(tc + 1, result))

