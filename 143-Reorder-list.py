# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count=0
        temp=head
        while temp!=None:
            temp=temp.next
            count+=1
        if count<3:
            return head
        mid=math.ceil(count/2)
        cur=head
        prev=ListNode(0)
        for i in range(mid):
            prev=cur
            cur=cur.next
        prev.next=None
        while cur!=None:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        temp=head
        for i in range(math.floor(mid//2)*2):
            nxt1=temp.next
            nxt2=prev.next
            temp.next=prev
            prev.next=nxt1
            temp=nxt1
            prev=nxt2
        return head

# Another approach
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge two halves
        first = head
        second = prev

        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2
