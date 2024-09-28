def fence(n,k,heights):
    List_of_hights= []
    sum = 0
    
    for i in range(k):
        sum = sum + heights[i]
    List_of_hights.append(sum)
    for i in range(k,n):
        sum = sum + heights[i]- heights[i-k]
        List_of_hights.append(sum)
    min_height = min(List_of_hights)
    print(List_of_hights.index(min_height)+1)
    
n, k = map(int, input().split())
heights = list(map(int, input().split())) 
fence(n,k, heights)