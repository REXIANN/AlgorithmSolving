# 1491.py 원재의 벽 꾸미기
import sys
sys.stdin = open("1491input.txt", "r")
# 1x1타일 N개를 사용해 RxC크기의 직사각형 인테리어를 만들어 벽을 꾸민다.
# 방은 정사각형으로 직사각형을 최대한 정사각형에 가깝게 만들면서, 
# 최대한 많은 타일을 사용하려고 한다.
# 가중치 = A x |R - C| + B x (N - R x C) 가 최소화된 값을 출력

for tc in range(int(input())):
    N, A, B = tuple(map(int, input().split()))
    V = A * B * 2
    for r in range(1, N+1):
        for c in range(r, N+1):
            if N - r * c < 0:break
            R = A * abs(r - c) + B * (N - r * c)
            V = R if R < V else V
    print('#{} {}'.format(tc+1, V))
