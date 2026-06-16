# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=l1,l2
        num1,num2=0,0
        c1,c2=0,0
        while temp1!=None:
            num1=num1+temp1.val*(10**c1)
            c1+=1
            temp1=temp1.next
        while temp2!=None:
            num2=num2+temp2.val*(10**c2)
            c2+=1
            temp2=temp2.next
        tot=num1+num2
        head = ListNode(tot % 10)
        tot //= 10

        temp = head

        while tot > 0:
            temp.next = ListNode(tot % 10)
            tot //= 10
            temp = temp.next

        return head

#gpt solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
