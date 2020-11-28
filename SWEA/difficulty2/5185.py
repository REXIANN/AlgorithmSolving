# 5185.py 이진수
import sys
sys.stdin = open("5185input.txt", "r")
#내꺼
for tc in range(int(input())): print('#{} {}'.format(tc + 1, ''.join(['{:04b}'.format(int(s, 16)) for s in input().split()[1]])))

## 세종이꺼
T = int(input())
for tc in range(1, T+1):
    N, num = map(str, input().split())
    result = bin(int(num, 16))[2:].zfill(4*int(N))
    print('#{} {}'.format(tc, result))


## 용준이꺼
for t in range(1, int(input()) + 1):
    N, hex_num = input().split()
    result = ''
    for num in hex_num:
        if '0' <= num <= '9':
            temp = ord(num) - ord('0')
        else:
            temp = ord(num) - ord('A') + 10
        for i in range(3, -1, -1):
            if temp & (1 << i):
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(t, result))
