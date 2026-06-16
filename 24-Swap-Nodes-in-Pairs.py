# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        cur=head
        nxt=head.next
        temp=nxt.next
        nxt.next=cur
        cur.next=temp
        head=nxt
        cur,nxt=nxt,cur
        temp1=nxt
        while cur!=None and nxt.next!=None:
            if nxt.next.next==None:
                return head
            cur,nxt=cur.next.next,nxt.next.next
            temp=nxt.next
            nxt.next=cur
            cur.next=temp
            cur,nxt=nxt,cur
            temp1.next=cur
            temp1=nxt
        return head

# Other solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next
