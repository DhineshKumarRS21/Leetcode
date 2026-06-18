# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        temp = head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        temp = head
        last = head

        if count != 0:
            k = k % count

        for _ in range(k):
            last = last.next

        while last.next is not None:
            last = last.next
            temp = temp.next

        last.next = head
        head = temp.next
        temp.next = None

        return head
#approach 2
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head

        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
