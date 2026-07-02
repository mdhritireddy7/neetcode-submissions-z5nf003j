# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        tortoise = head
        hare = head

        while True:
            tortoise = tortoise.next
            hare = hare.next 

            if not hare or not (hare.next):
                return False
            else:
                hare = hare.next

            if tortoise == hare:
                return True
        