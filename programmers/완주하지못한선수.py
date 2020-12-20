def solution(participant, completion):
    set_comp = set(completion)
    for partic in participant:
        if partic not in set_comp:
            return partic
    
    part_dict = {}
    for partic in participant:
        if part_dict.get(partic):
            part_dict[partic] += 1
        else: 
            part_dict[partic] = 1
    
    comp_dict = {}
    for comp in completion:
        if comp_dict.get(comp):
            comp_dict[comp] += 1
        else:
            comp_dict[comp] = 1
    
    for d in part_dict.keys():
        if part_dict[d] != comp_dict[d]:
            return d