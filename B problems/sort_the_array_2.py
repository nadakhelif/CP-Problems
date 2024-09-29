def sort_the_array():
    n = int(input())
    a = list(map(int, input().split()))
    
    sorted_a = sorted(a)
    
    if a == sorted_a:
        print("yes")
        print(1, 1)
        return
    
    left, right = 0, n - 1
    
    # Find the first index where a and sorted_a differ
    while left < n and a[left] == sorted_a[left]:
        left += 1
        
    while right >= 0 and a[right] == sorted_a[right]:
        right -= 1
    if left < right:
        a[left:right + 1] = a[left:right + 1][::-1]
    
    if a == sorted_a:
        print("yes")
        print(left + 1, right + 1)  
    else:
        print("no")

sort_the_array()
