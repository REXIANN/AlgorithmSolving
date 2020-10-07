from itertools import combinations 
def solution(orders, course):
    d = {}
    for order in orders:
      for ord in order:
        if d.get(ord):
          d[ord] += 1
        else:
          d[ord] = 1
    # print(d)
    rm = [ x for x in d.keys() if d[x] == 1]
    # print(rm)
    
    d = {}
    for order in orders:
      ordre = [o for o in order]
      ordre.sort()
      for cours in course:
        for r in rm:
          if r in ordre:
            ordre.remove(r)

        if cours > len(ordre):
          pass
        else:
          for x in combinations(ordre, cours):
            
            if d.get(x):
              d[x] += 1
            else:
              d[x] = 1

    # print('dict', d)

    answers = [[] for _ in range(len(course))]
    for i in range(len(course)):
        max_v = 0
        for key, value in d.items():
            if len(key) == course[i]:
                # print(key)
                if value > 1 and value > max_v:
                    answers[i] = [key]
                    max_v = value
                elif value == max_v:
                    answers[i].append(key)
        # print()

    result = [''.join(ans) for answer in answers for ans in answer]  
    result.sort()          
    # print('ANS', result)
    return result


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))