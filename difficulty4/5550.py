# 5550.py 나는 개구리로소이다

import sys
sys.stdin = open("5550input.txt", "r")


tc = int(input())

for test_count in range(1, tc + 1):
    dict_ = {'c': 0,'r': 1,'o': 2,'a': 3,'k': 4}
    print('#{}'.format(test_count), end=" ")
    string = input()
    numbers = [dict_[char] for char in  string]    
    idx, count, frog_count = 0, 0, 0
    ch = 0
    if len(numbers) % 5 != 0:
        print(-1)
        continue

    while len(numbers) > 0:
        if numbers[idx] == ch:
            del numbers[idx]
            ch += 1
            if ch == 5:
                frog_count += 1
                ch %= 5
        else:
            idx += 1

        if idx == len(numbers):
            if ch == 0 and frog_count != 0:
                idx = 0
                count += 1
                frog_count = 0
            else:
                count = -1
                break  
    
    print(count)