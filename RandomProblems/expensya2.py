array = [14,10,6,8,5,3]
s = 11
array.sort()
l=0
r=len(array)-1
while(l<r):
    if array[l]+array[r]==s:
        print(array[l],array[r])
        break
    if array[l]+array[r]<s:
        l+=1
    if array[l]+array[r]>s:
        r-=1

         