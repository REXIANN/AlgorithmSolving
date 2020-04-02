# 1289.py 원재의 메모리 복구하기
import sys
sys.stdin = open("1289input.txt", "r")

for tc in range(int(input())):
    L = input()
    count, x = 0, '1'
    for i in L:
        if i == x:
            count += 1
            x = '0' if int(x) else '1'     
    print('#{} {}'.format(tc+1, count))