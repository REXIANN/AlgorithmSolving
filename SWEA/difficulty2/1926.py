# -*- coding: utf-8 -*-

# 간단한 369 게임

# 3,6,9가 하나도 없으면 그냥 숫자 출력
# 있으면 있는 만큼 '-' 출력


initial_num = input()
target = '369'

for i in range(1, int(initial_num) + 1): 
    count = 0
    for j in str(i):
        if j in target:
            count += 1
    
    if count:
        for _ in range(count):
            print('-', end='')
        print(' ', end='')
    else:
        print(i, end=' ')
    
    

       
    