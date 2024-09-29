def sort_the_array():
    n = int(input())
    a = list(map(int, input().split()))
    a1 = a[:]
    sorted_a = sorted(a)
    sorted_a1 = sorted_a[:]
    if a == sorted_a:
        print("yes")
        print(1, 1)  
        return
    condition = True
    while(condition== True):
        if a1[-1] == sorted_a1[-1]:
            a1 = a1[:-1]
            sorted_a1 = sorted_a1[:-1]
            
        else :
            index_max = a1.index(max(a1))
            a1_reversed = a1[index_max:][::-1] 
            a1_new = a1[:index_max] + a1_reversed + a[index_max + len(a1_reversed):]
            if sorted_a == a1_new:
                print("yes")
                
                print(index_max + 1, len(a1))
                condition = False 
            else:
                print("no")
                condition = False  
sort_the_array()
            
             
        
    
    
    
