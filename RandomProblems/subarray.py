max_int=-1000
somme_subarray=0
l=[-2,-3,4,-1,-2,1,5,-3]
for i in l:
    somme_subarray+=i
    if(max_int<somme_subarray):
        max_int=somme_subarray      
    if(somme_subarray<0):
        somme_subarray=0
print(max_int)
        
        
        