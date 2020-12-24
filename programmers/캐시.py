from collections import deque

def solution(cacheSize, cities):
    h = [[0, 'a'] for _ in range(cacheSize)]
    h_set = set()
    count = 0
    # heapq를 직접 구현하는게 핵심 

    for city in cities:
        city = city.lower()
        if city in h_set:
            for hh in h:
                if hh[1] == city:
                    hh[0] += 1
                    break
            count += 1
        else:
            if h:
                rm = heapq.heappop(h)
                if rm[1] in h_set:
                    h_set.remove(rm[1])
            heapq.heappush(h, [1, city])
            h_set.add(city)
            count += 5
        print(h, count)
    
    return count

cacheSize = 2

cities1 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
cities2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
cities6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

print(solution(cacheSize, cities3))