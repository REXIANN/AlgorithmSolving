# 5120.py 암호
import sys
sys.stdin = open("5120input.txt", "r")

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    array = list(map(int, input().split()))
    idx = M 
    for _ in range(K):
        if idx == N:
            num = array[idx - 1] + array[0]
        elif idx > N:
            idx -= N
            num = array[idx] + array[idx - 1]
        else:
            num = array[idx] + array[idx - 1]
        array.insert(idx, num)
        N += 1
        idx += M
    array.reverse()
    result = ' '.join(list(map(str, array[:10])))
    print('#{} {}'.format(tc + 1, result))