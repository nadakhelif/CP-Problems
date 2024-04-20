def subArraySum(arr, n, s): 
    i = 1 
    l = []
    l.append(arr[0])
    found = 1
    while(i < n and found):
        l.append(l[i-1] + arr[i])
        if(l[i] == s):
            print(1, i+1)
            found = 0
        i += 1
    seti = set(l)
    print(seti)
    if(found==1):
        for i in range(len(l)):
            if l[i] < s:
                continue
            else:
                oop= l[i]-s
                if oop in seti:
                    indice=oop
                    print(indice, i+1)
                    break
        print(-1)
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2=[1,2,3,7,5]
subArraySum(l2, 5, 12)


class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       
        if s == 0:
            return [-1]
        left = 0
        right = 0
        current_sum = arr[0]
        while right < n:
            if current_sum == s:
                return [left+1, right+1]
            elif current_sum < s:
                right += 1
                if right < n:
                    current_sum += arr[right]
            else:
                current_sum -= arr[left]
                left += 1
        return [-1]