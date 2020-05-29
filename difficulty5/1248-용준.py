import sys
sys.stdin = open("1248input.txt", "r")

def distance_root_node(n):
    q = parent[n]
    d = 0
    while q != 1:
        q = parent[q]
        d += 1
    return d
 
 
def common_parent(n1, n2, d1, d2):
    parent1 = parent[n1]
    parent2 = parent[n2]
    while parent1 != parent2:
        if d1 > d2:
            parent1 = parent[parent1]
            d1 -= 1
        elif d1 < d2:
            parent2 = parent[parent2]
            d2 -= 1
        else:
            parent1 = parent[parent1]
            parent2 = parent[parent2]
    return parent1
 
 
for t in range(1, int(input())+1):
    V, E, n_1, n_2 = map(int, input().split())
    link_list = list(map(int, input().split()))
    parent = [0] * (V + 1)
    child = [[]*(V+1) for _ in range(V+1)]
    for i in range(E):
        start = link_list[2 * i]
        end = link_list[2 * i + 1]
        parent[end] = start
        child[start].append(end)
    d_1 = distance_root_node(n_1)
    d_2 = distance_root_node(n_2)
    com_p = common_parent(n_1, n_2, d_1, d_2)
    node_size = len(child[com_p]) + 1
    node = child[com_p]
    while node:
        c_node = child[node.pop()]
        node_size += len(c_node)
        node += c_node
    print('#{} {} {}'.format(t, com_p, node_size))
