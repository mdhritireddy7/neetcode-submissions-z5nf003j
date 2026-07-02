# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        first = head
        second = prev

        while second:
            firstNext = first.next
            first.next = second
            first = firstNext

            secondNext = second.next
            second.next = firstNext
            second = secondNext





        
        
