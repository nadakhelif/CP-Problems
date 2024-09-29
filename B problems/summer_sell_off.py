n,k=map(int,input().split())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
l.sort(key=lambda y:min(2*y[0],y[1])-min(y[0],y[1]))
s=0
for i in range(n):
    if n>k:
        s+=min(l[i][0],l[i][1])
    else:
        s+=min(2*(l[i][0]),l[i][1])
    n-=1
print(s)        
 
 