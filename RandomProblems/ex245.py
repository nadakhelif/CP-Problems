N=3
K=3
A=[1,2,3]

leftMax = [A[0]] + [0] * (N-2)
print(leftMax)
rightMin = [0] * (N-2) + [A[N-1]]
print(rightMin)
for i in range(1, N-1):
    leftMax[i] = max(leftMax[i-1], A[i])
    
for i in range(N-3, -1, -1):
    rightMin[i] = min(rightMin[i+1], A[i+1])
print(rightMin)
print(leftMax)
count = 0
for i in range(N-1):
    if leftMax[i] + rightMin[i] >= K:
        count += 1
print (count)