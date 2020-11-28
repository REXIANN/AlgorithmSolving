# 4408.py 자기 방으로 돌아가기
import sys
sys.stdin = open("4408input.txt", "r")
def f(i):
    return int(i)//2 + 1 if int(i)%2 else int(i)//2

for tc in range(int(input())):
    N = int(input())
    R = [tuple(map(f, input().split())) for _ in range(N)]
    M, U = [0] * 201, [0] * N
    count = 1

    for i in range(N):
        if U[i]: continue 
        U[i] = 1
        
        a1, a2 = min(R[i]), max(R[i]) 
        for j in range(a1, a2+1): M[j] = 1

        for j in range(i+1, N):
            b1, b2 = min(R[j]), max(R[j])
            for k in range(b1, b2+1):
                if M[k]: break
                M[k] = 1
            else:
                U[j] = 1
        
        M = [0] * 201
        if min(U) == 0: count += 1

    print('#{} {}'.format(tc+1, count))


# T = int(input())
# for t in range(T):
#     N = int(input())
#     cnt = [0] * 201 # 1~ 200 번호
#     for n in range(N):
#         a, b = list(map(int,input().split())) # A --> B
       
#         a = (a+1)//2
#         b = (b+1)//2

#         if a > b: a, b = b, a
#         for i in range(a,b+1):
#             cnt[i] += 1
        
#     print('#{}'.format(t+1),max(cnt))