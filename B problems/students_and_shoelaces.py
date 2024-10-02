from collections import defaultdict
n , m =map(int,input().split()) 

visited = defaultdict(set)
for _ in range(m):
    a,b=map(int,input().split())
    visited[a].add(b) 
    visited[b].add(a)

s_discarded = set()
number_of_groups=0
while True:
    found_len_1 = False
    for key, value_set in visited.items():
        if len(visited[key]) == 1 :
            s_discarded.add(key)
            found_len_1 = True
    if found_len_1 : 
        number_of_groups +=1   
    else :
        break        
    for v in s_discarded:
        del visited[v]
    for v in s_discarded:
        for key, value_set in visited.items():
            value_set.discard(v)
    s_discarded=set()
            
print(number_of_groups)
        
        
        