str="/a//"
l=str.split('/')
print(l)
i=0
while(i<len(l) ) :
    print(i)
    if (l[i]==''):
        l.remove(l[i])
        i=i
    else :
        i+=1 
print (l)
p=[]
l=['a']
for i in l :
        if i!= ".":
            if i!="..":
                p.append(i)
            elif(len(p)!=0): 
                p.pop()
            
pa='/'.join(p)
pa="/"+pa
print (pa)
