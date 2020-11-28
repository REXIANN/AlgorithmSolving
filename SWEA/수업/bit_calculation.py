def bin_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%3d = " %i, end='')
    bin_print(i)

bin_print(4)
bin_print(15)
bin_print(20)