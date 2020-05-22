adic = {}
ls = ['a', 'b', 'c', 'b', 'c', 'k']

for char in ls:
    if char in adic.keys():
        adic[char] += 1
    else:
        adic[char] = 1
    
print(adic)
print(max(adic.values()))
