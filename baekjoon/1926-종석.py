import sys
sys.stdin = open('picture.txt')

n, m = map(int,input().split())
lst = [list(map(int,input().split())) for __ in range(n)]
visit_lst = [[0] * m for __ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
number = 0
stack = []
final_count = []

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and visit_lst[i][j] == 0:
            count = 1
            number = number + 1
            visit_lst[i][j] = 1
            stack.append((i,j))
            while stack:
                k = stack.pop()
                for q in range(4):
                    di = k[0] + dx[q]
                    dj = k[1] + dy[q]

                    if 0 <= di < n and 0 <= dj < m:
                        if lst[di][dj] == 1 and visit_lst[di][dj] == 0:
                            visit_lst[di][dj] = 1
                            stack.append((di,dj))
                            count = count + 1
            final_count.append(count)

if len(final_count) != 0:
    print(number)
    print(max(final_count))
else:
    print(0)
    print(0)






