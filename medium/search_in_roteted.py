class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(nums==None or len(nums)==0) :
            return -1
        l=0
        r=len(nums)-1
        m=0
       
        while(l<r):
            m = (l+r)//2
            if(nums[m] > nums[r]):
                l = m+1
            else:
                r = m
            
        
      
        s = l
        l = 0
        r = len(nums)-1
        if(target >= nums[s] and target <= nums[r]):
            l = s
        else:
            r = s
        
        
        while(l<=r):
            m = (l+r)//2
            if(nums[m]==target) :
                return m
            elif(nums[m] > target) :
                r = m-1
            else: l=m+1
        
        
        return -1