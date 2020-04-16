# 5122.py 수열 편집
import sys
sys.stdin = open("5122input.txt", "r")

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))
    for _ in range(M):
        command = list(input().split())
        if command[0] == 'I':
            idx, value = int(command[1]), int(command[2])
            array.insert(idx, value)
        elif command[0] == 'C':
            idx, value = int(command[1]), int(command[2])
            array[idx] = value
        else:
            idx = int(command[1])
            array.pop(idx)
    
    result = -1 if L > len(array) else array[L]
    print('#{} {}'.format(tc + 1, result))