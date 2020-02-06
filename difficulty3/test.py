num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(num_list)
zip_num_list = list(zip(*num_list))
print(zip_num_list)
zip_num_list = list(map(list, zip(*num_list)))
print(zip_num_list)
zip_num_list = tuple(map(list, zip(*num_list)))
print(zip_num_list)