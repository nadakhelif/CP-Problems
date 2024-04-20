class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if(N==0):
            return -1
        if(N==1):
            return 1
            
        l=[]
        l.append(A[0])
        for i in range(1,len(A)):
            l.append(l[i-1]+A[i])
        for i in range(1,len(A)):
            if l[i-1]==(l[N-1]-l[i]):
                return i+1
        if i==N-1 :
            return -1
        