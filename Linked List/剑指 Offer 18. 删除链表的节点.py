# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        leftnode = head
        rightnode = head.next
        while rightnode:
            if rightnode.val == val:
                leftnode.next = rightnode.next
                rightnode = rightnode.next
            else:
                rightnode = rightnode.next
                leftnode = leftnode.next
        return head