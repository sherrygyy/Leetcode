# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        leftnode = rightnode = head
        count = 0
        while count < k:
            rightnode = rightnode.next
            count = count + 1
        if not rightnode:
            return head
        while rightnode:
            rightnode = rightnode.next
            leftnode = leftnode.next
        return leftnode
