# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        right =  left = head
        count = 0
        while count < n:
            right = right.next
            count = count + 1
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head