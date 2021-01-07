import sys
sys.stdin = open('18405input.txt', 'r')

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())

print(N, K, s, x, y)
print(matrix)

visited = [[False] * N for _ in range(N)]

print(visited)

# for _ in range(s):
#     for i in range(1, k + 1):
#         for r in range(N):
#             for c in range(N):
                # oh no!