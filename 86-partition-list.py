class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev1=dummy
        cur1=prev1.next
        while cur1 and cur1.val < x:
            cur1 = cur1.next
            prev1 = prev1.next

        if cur1 is None:
            return head
        cur=cur1
        prev=prev1
        while cur!=None:
            if cur.val<x:
                prev.next=cur.next
                prev1.next=cur
                cur.next=cur1
                prev1=prev1.next
                cur=prev.next
            else:
                cur=cur.next
                prev=prev.next
        return dummy.next
