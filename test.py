from time import time

num_list = [i for i in range(1, 10 ** 8)]
num_set = set(i for i in range(1, 10 ** 8))

print("Start analysis")
number = 10 ** 8 - 3
start_time = time()
if number in num_list:
    print("number is in num_list")
    print(time() - start_time)

start_time = time()
if number in num_set:
    print("number is in num_set")
    print(time() - start_time)