def solution(s):
    zero_count = 0
    count = 0
    while True:
        one_count = 0
        one_list = []
        for ss in s:
            if ss == '1':
                one_count += 1
                one_list.append(ss)
            else:
                zero_count += 1
        
        count += 1
        
        if one_count == 1:
            return [count, zero_count]
        
        s = "{:b}".format(len(one_list))