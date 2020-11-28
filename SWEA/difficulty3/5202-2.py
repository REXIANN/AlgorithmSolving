# 5202.py 
import sys
sys.stdin = open("5202input.txt", "r")

for tc in range(int(input())):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    numbers.sort(key=lambda x : x[1])
    
    # print(numbers)
    count = 0
    start = 0
    for i in range(N):
        if numbers[i][0] >= start:
            count += 1
            start = numbers[i][1]
            
    print('#{} {}'.format(tc + 1, count))
