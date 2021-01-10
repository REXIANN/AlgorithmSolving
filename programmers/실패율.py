def solution(N, stages):
    stages.sort()
    rate_dict = dict()
    total = len(stages)
    idx = 0
    while idx != len(stages):
        val = stages[idx]
        count = 1
        while idx + 1 < len(stages) and stages[idx + 1] == val:
            idx += 1
            count += 1
        if rate_dict.get(count/total):
            rate_dict[count/total].append(val)
        else:
            rate_dict[count/total] = [val]
        total -= count
        idx += 1
        
    stage_set = set(i for i in range(1, N + 1))
    keys = sorted([key for key in rate_dict.keys()], reverse=True)
    
    answer = []
    for key in keys:
        stage = rate_dict[key]
        for sta in stage:
            if sta > N:
                continue
            else:
                answer.append(sta)
                stage_set.remove(sta)
    
    rest_stages = list(stage_set)
    answer.extend(rest_stages)
    return answer