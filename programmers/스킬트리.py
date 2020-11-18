def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        skill_set = set([i for i in skill])
        tree_set = set()
        idx = 0
        for tree in skill_tree:
            char = skill[idx]
            if char in skill_set:
                skill_set.remove(char)

            print(tree, char, skill_set, tree_set)
            if tree != char:
                tree_set.add(tree)
            else:
                idx += 1
                if idx == len(skill):
                    idx -= 1
            if tree in skill_set:
                break
        else:
            count += 1
            print(skill_set, tree_set)
            
    return count

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))