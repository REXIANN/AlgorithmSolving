# 5110.py 수열 합치기
import sys
sys.stdin = open("5110input.txt", "r")

def check(array, X):
    for i in range(len(array)):
        if X < array[i]:
            return i
    return len(array)


for tc in range(int(input())):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(M - 1):
        array2 = list(map(int, input().split()))
        idx = check(array, array2[0])
        array[idx:idx] = array2
    result = ' '.join(map(str, array[-1:-11:-1]))
    print('#{} {}'.format(tc + 1, result))