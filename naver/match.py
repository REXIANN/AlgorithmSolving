numbers = []
matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def bt(lower_range, upper_range, cnt, number):
    if cnt < 0:
        return
    
    if cnt == 0:
        numbers.append(number)
        return

    for i in range(lower_range, upper_range):
        if cnt - matches[i] >= 0:
            this_number = 10 * number + i 
            bt(0, 10, cnt - matches[i], this_number)
    

k = 40
bt(1, 10, k, 0)
print(len(numbers))
