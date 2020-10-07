# from itertools import combinations 
# def solution(orders, course):
#     order_dict = {}
#     for i in range(len(orders)):
#       for ord in orders[i]:
#         if order_dict.get(ord):
#           order_dict[ord].add(i + 1)
#         else:
#           order_dict[ord] = {i + 1,}
#     print(order_dict)
    
#     for cours in course:
#       ss = []
#       for menu, times in order_dict.items():
#         if len(times) > 1 and len(times) >= cours:
#           ss.append(menu)
#       print(ss)
#       for new_menu in combinations(ss, cours):
#         print(new_menu)
#     print(order_dict)


    
#     answer = []
#     return answer
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]

 
print()      
        