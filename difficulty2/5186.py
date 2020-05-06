# 5186.py 이진수2
import sys
sys.stdin = open("5186input.txt", "r")

for tc in range(int(input())):
    num = float(input())
    result = ''
    check = 0.5
    for i in range(13):
        if num == 0:break
        result += '0' if check > num else '1'
        num = num if check > num else num - check
        check /= 2
    print('#{}'.format(tc + 1), end=' ')
    print(result if num == 0 else 'overflow')

