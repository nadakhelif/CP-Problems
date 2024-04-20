def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
        if (len(pushed)==0 and len(popped)==0 ):
            return True 
        if(len(pushed)==0 or len(popped)==0 ):
            return False
        i=0
        while i < len(pushed):
            if(i==len(pushed)-1):
                return
            if(pushed[i]!=popped[0]):
                i+=1
            else:
                print(pushed)
                print(popped)
                pushed.pop(i)
                popped.pop(0)
                return(validateStackSequences(pushed,popped))
pushed=[1,2,3,4,5]
popped=[4,3,5,1,2]
            

print(validateStackSequences(pushed, popped))