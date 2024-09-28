def coins():
    count = {'A': 0, 'B': 0, 'C': 0}
    comparisons = [input().strip() for _ in range(3)]

    for comp in comparisons:
        if comp[1] == '>': 
            count[comp[0]] += 1
        else:  
            count[comp[2]] += 1

    if sorted(count.values()) == [0, 1, 2]:
        result = ''.join(sorted(count, key=lambda x: count[x]))
        print(result)
    else:
        print("Impossible")
coins()        