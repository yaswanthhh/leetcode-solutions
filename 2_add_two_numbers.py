# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        carry = 0

        while l1 is not None or l2 is not None or carry!=0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            curr_sum = val1+val2+carry

            digit = curr_sum%10
            carry = curr_sum//10

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head.next
