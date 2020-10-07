# 5108.py 숫자 추가
import sys
sys.stdin = open("5108input.txt", "r")

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(M):
        idx, value = map(int, input().split())
        array.insert(idx, value)
    
    print(array[L])