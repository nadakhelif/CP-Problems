

def splitnumber(n):
    l=[]
    k=n
    while(k!=0):
        reste=k%10
        k=k//10
        
        l.append(reste)
    return l
n=5
 
carre_somme=n
previous=set()
while(carre_somme not in previous):
    previous.add(carre_somme)
    print(carre_somme)
    
    l=splitnumber(carre_somme)
    carre_somme=0
    for i in l:
        carre_somme=carre_somme+i*i
    if(carre_somme==1):
        print("true")
        break
if carre_somme in previous:
    print("false")
    
    
        

    
    