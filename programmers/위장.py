from itertools import combinations

def solution(clothes):
    cloth_dict = {}
    total = 0
    for cloth in clothes:
        if cloth_dict.get(cloth[1]):
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1
    if sum([cloth_dict[key] for key in cloth_dict.keys()]) == len(cloth_dict):
        return 2 ** (len(cloth_dict)) - 1
    elif len(cloth_dict) == 1:
        return sum(cloth_dict.values())
    else:
        for i in range(1, len(cloth_dict) + 1):
            for combination in combinations(cloth_dict, i):
                value = 1
                for com in combination:
                    value *= cloth_dict[com]
                total += value
        
    return total