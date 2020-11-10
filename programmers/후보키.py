from itertools import combinations

def solution(relations):
    columns = [[] for _ in range(len(relations[0]))]
    for relation in relations:
        for i in range(len(relation)):
            columns[i].append(relation[i])
    
    minimality = set(i for i in range(len(columns)) if len(columns[i]) == len(set(columns[i])))
    second_mini = set()
    if len(columns) == 1:
      return len(minimality)
    # print(minimality)        
       
    for i in range(2, len(columns) + 1):
      for combination in combinations([j for j in range(len(columns))], i):
        # 만일 존재한다면 유일성이 깨지므로 패스
        
        if minimality.intersection(combination):
            continue
        # print(combination)
        select_set = set(tuple(columns[j][i] for j in combination) for i in range(len(columns[0])))
        # print(select_set)
        if len(select_set) == len(columns[0]):
            second_mini.add(combination)
    
    # print(minimality, second_mini)
    mini_list = list(second_mini)
    sub_mini = set()
    for i in range(0, len(mini_list) - 1):
        for j in range(i + 1, len(mini_list)):
            # print(mini_list[i], mini_list[j])
            a = set(mini_list[i])
            b = set(mini_list[j])
            # print(a, b)
            if a.issubset(b):
                sub_mini.add(mini_list[j])
    xx = second_mini.difference(sub_mini)
    return len(minimality) + len(xx)


relations = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relations))