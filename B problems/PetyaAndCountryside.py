def max_watered_sections(n, heights):
    max_watered = 0
    
    for i in range(n):
        left_count = 0
        for j in range(i, 0, -1): 
            if heights[j] >= heights[j-1]:
                left_count += 1
            else:
                break
        right_count = 0
        for j in range(i, n-1):
            if heights[j] >= heights[j+1]:
                right_count += 1
            else:
                break

        total_watered = left_count + right_count + 1
        max_watered = max(max_watered, total_watered)

    print(max_watered) 

n = int(input())  
heights = list(map(int, input().split())) 
max_watered_sections(n, heights)