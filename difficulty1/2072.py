# -*- coding: utf-8 -*-

num_list = []
result_list = []
count_num = int(input())

for _ in range(count_num):
    num_list.append(input())

for i in range(count_num):
    num_str = []
    sum_ = 0
    num_str = num_list[i].split()
 
    for j in num_str:
        if int(j) % 2 == 1:
            sum_ += int(j) 
          
    result_list.append(sum)

for i in range(count_num):
    print(f'#{i+1} {result_list[i]} ')
