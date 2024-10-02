n= input()
n= int(n)
heights =input()
heights = list(map(int, heights.split()))
heights.sort()
if(n>=3):
    found = False
    for i in range(n-1,1,-1):
        if heights[i]+heights[i-1]> heights[i-2] and heights[i-1]+heights[i-2]> heights[i] and heights[i]+heights[i-2]> heights[i-1] :
            found = True  # Set flag to True if condition is met
            print("YES")
            break 
    if not found:
        print("NO")    
else:            
    print("NO")        
    