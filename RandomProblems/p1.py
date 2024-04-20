
n=int (input())
l2=list
for i in range(n):
    n1= int (input())
    l1= list (input())
    for j in range(n1-1):
        l2[j]=l1[j]+l1[j+1]
    print(l2)    