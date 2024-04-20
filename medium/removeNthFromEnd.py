class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h=head
        l=0
        if(head==None):
            return h
        l=1
        while(h.next!=None):
            h=h.next
            l+=1
        if(l==n):
            return head.next
        h=head
        h1=head.next
        i=1
        if(h1==None):
            return h1
        while(i<l-n):
            i+=1
            
            h=h1
            h1=h1.next
        h.next=h1.next
        return head