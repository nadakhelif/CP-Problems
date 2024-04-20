import sys
 
# O(n * k) solution for finding
# maximum sum of a subarray of size k
INT_MIN = -sys.maxsize - 1
print(INT_MIN)
 
mot="nada"

brokenkey=['b']
s=set(brokenkey)
def canWrite(mot,brokenKey):
    i=0
    while(i<len(mot)):
        if mot[i] in brokenKey :
            return False 
        else :
            i+=1
    if i==len(mot) :
        return True

print(canWrite(mot,s))
            
            