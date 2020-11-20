from collections import deque
import heapq

def solution(cacheSize, cities):
    cache = []
    cache_set = set()
    count = 0
    if not cacheSize:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache_set:
            count += 5
            for i in range(len(cache)):
                if cache[i][1] == city:
                    cache[i][0] += 1

            
        else:
            count += 1
            if len(cache_set) == cacheSize:
                del_city = heapq.heappop(cache)
                cache_set.remove(del_city[1])
            heapq.heappush(cache, [1, city])
            cache_set.add(city)
            
    return count


cacheSize = 3	
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
# 50
# cacheSize = 3	
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	
# # 21
# cacheSize = 2	
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# # 60
# cacheSize = 5	
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# # 52
# cacheSize = 2	
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]	
# # 16
# cacheSize = 0	
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
# # 25
print(solution(cacheSize, cities))