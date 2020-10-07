# 5986.py 새샘이와 세 소수
import sys
sys.stdin = open("5986input.txt", "r")

def backtrack(c, k, N, s=0):
    global count
    if s > N or c > 3: 
        return
    
    if c == 3 and s == N:
        count += 1
    else:    
        for i in range(k, len(prime_numbers)):
            backtrack(c + 1, i, N, s + prime_numbers[i])


for tc in range(int(input())):
    N = int(input())
    prime_numbers = [2]
    count = 0
    for i in range(2, N + 1):
        for j in range(len(prime_numbers)):
            if i % prime_numbers[j] == 0:
                break
        else: 
            prime_numbers.append(i)
    backtrack(0, 0, N)
    print('#{} {}'.format(tc + 1, count))
