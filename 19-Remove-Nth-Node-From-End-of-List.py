class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        if count == n:
            return head.next

        temp = head
        node = count - n

        while node > 1:
            node -= 1
            temp = temp.next

        temp.next = temp.next.next

        return head
