import heapq

def solution(cacheSize, cities):
    h = [] # 사용빈도, 시간, 값
    count = 0

    print(h)
    for city in cities:
        city = city.lower()
        print(city)
        for i in range(len(h)):
            h[i][1] -= 1
        
        is_heap_empty = True
        for i in range(len(h)):
            if h[i][2] == city:
                h[i][0] -= 1
                h[i][1] = len(cities)
                is_heap_empty = False
                count += 1
                break
        
        if is_heap_empty:
            count += 5
            if cacheSize == 0:
                continue

            if len(h) < cacheSize:
                h.append([len(cities), len(cities), city])
                print('result', h)
                continue

            remove_candidats = []
            heapq.heapify(h)

            first_h = heapq.heappop(h)
            remove_candidats.append(first_h)
            freq = first_h[0]
            while h:
                heapq.heapify(h)
                if h[0][0] == freq:
                    hh = heapq.heappop(h)
                    remove_candidats.append(hh)
                else:
                    break
            # print('h', h, 'rm', remove_candidats)
            for i in range(len(remove_candidats)):
                remove_candidats[i][0], remove_candidats[i][1] = remove_candidats[i][1], remove_candidats[i][0]
            # print('chrm', remove_candidats)
            heapq.heapify(remove_candidats)
            heapq.heappop(remove_candidats)
            for i in range(len(remove_candidats)):
                remove_candidats[i][0], remove_candidats[i][1] = remove_candidats[i][1], remove_candidats[i][0]
            
            heapq.heappush(h, [len(cities), len(cities), city])
            # print('changed', remove_candidats)
            for rm in remove_candidats:
                h.append(rm)
        print('result', h)
        print('count', count)           
    
    return count

cacheSize = 5

cities1 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
cities2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
cities6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

print(solution(cacheSize, cities4))