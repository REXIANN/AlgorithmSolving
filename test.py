from time import time

num_list = [i for i in range(1, 10 ** 7)]
num_set = set(i for i in range(1, 10 ** 7))

print('Start analysis')
number = 1#5 * 10 ** 6
start_time = time()
if number in num_list:
    print('number is in num_list: ', end='')
    print(time() - start_time)

start_time = time()
if number in num_set:
    print('number is in num_set : ', end='')
    print(time() - start_time)