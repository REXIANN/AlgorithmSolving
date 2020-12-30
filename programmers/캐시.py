from collections import deque

def solution(cacheSize, cities):
    heap = [[0, 0, 'a'] for _ in range(cacheSize)] # 사용빈도, 시간, 값
    is_heap_empty = True
    
    for city in cities:
        city = city.lower()
        print(city)

        for h in heap:
            h[1] += 1

        
        for i in range(cacheSize):
            if h[i][2] == city:
                h[i][0] += 1
                is_heap_empty = False
                break
        
        if is_heap_empty:
            for i in range(cacheSize):
                min_value = len(cities)
                if h[i][1] < 

    
    return 1

cacheSize = 2

cities1 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
cities2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
cities6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

print(solution(cacheSize, cities3))