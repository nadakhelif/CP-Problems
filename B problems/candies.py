def candies(n, arr):
    previous = 1
    result = 1
    for i in range(1, len(arr)):
        if (arr[i]> arr[i-1]):
            previous +=1
        elif (arr[i]== arr[i-1] and previous>1):
            previous =1
        elif (arr[i]< arr[i-1]):
            previous =1
        else:
            previous = 1
        result += previous
    return result
        
candies(10,[2,4,2,6,1,7,8,9,2,1])