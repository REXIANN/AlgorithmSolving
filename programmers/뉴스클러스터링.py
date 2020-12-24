def solution(str1, str2):
    d_first, d_second = dict(), dict()
    answer = 0

    for i in range(len(str1) - 1): 
        x, y = str1[i], str1[i + 1]
        if not x.isalpha() or not y.isalpha():
            continue
        string = x.lower() + y.lower()
        if d_first.get(string):
            d_first[string] += 1
        else:
            d_first[string] = 1

    for i in range(len(str2) - 1):
        x, y = str2[i], str2[i + 1]
        if not x.isalpha() or not y.isalpha():
            continue
        string = x.lower() + y.lower()
        if d_second.get(string):
            d_second[string] += 1
        else:
            d_second[string] = 1

    key_first = [key for key in d_first.keys()]
    key_second = [key for key in d_second.keys()]
    
    if not len(key_first) and not len(key_second):
        return 65536
    
    key_set = set(key_first + key_second)
    numerator = []
    for key in key_set:
        if key in d_first and key in d_second:
            numerator.append(min(d_first[key], d_second[key]))
    
    denominator = []
    for key in key_set:
        if key in d_first or key in d_second:
            val1 = d_first[key] if d_first.get(key) else 0
            val2 = d_second[key] if d_second.get(key) else 0
            denominator.append(max(val1, val2))

    
    answer = sum(numerator) / sum(denominator)
    return int(answer * 65536)



str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2))