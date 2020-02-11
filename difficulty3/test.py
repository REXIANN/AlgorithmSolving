number = 1234567981
num_list = []
for i in range(1, 1234567892):
    if number % i == 0:
        num_list.append(i)

print(num_list)