s=list("helulo")

voy="aeyuio"
l=[]
for i in range(len(s)):
    if (s[i].lower() in voy ):
        l.append(i)
il=0 
ir=len(l)-1
while(il<ir):
    k=s[l[il]]
    s[l[il]]=s[l[ir]]
    s[l[ir]]=k
    il+=1
    ir-=1
print(''.join(s))

    

