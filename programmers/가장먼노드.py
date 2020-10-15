from collections import deque


def solution(n, edge):
    vertex_list = [[] for _ in range(n)]
    for ed in edge:
        x, y = ed[0] - 1, ed[1] - 1
        vertex_list[x].append(y)
        vertex_list[y].append(x)

    # bfs
    visited = set([0])
    list_one = vertex_list[0]
    for elem in vertex_list[0]:
        visited.add(elem)
    
    while list_one:
        count = len(list_one)
        list_two = []
        for elem in list_one:
            for el in vertex_list[elem]:
                if el not in visited:
                    visited.add(el)
                    list_two.append(el)
        
        list_one = list_two

    return count


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
a = solution(n, edge)
print(a)