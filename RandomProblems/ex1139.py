#User function Template for python3
class Solution:
    
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        
        curr_sum = sum(Arr[:K])
        max_sum = curr_sum

    # Slide the window and update the sum
        for i in range(K, N):
            curr_sum += Arr[i] - Arr[i-K]
            max_sum = max(max_sum, curr_sum)
    
        return max_sum