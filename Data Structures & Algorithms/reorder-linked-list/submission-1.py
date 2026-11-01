# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            fast = fast.next
        
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev

            prev = curr
            curr = nextt
        tail = prev
        
        curr = head
        while tail:
            curr_nextt = curr.next
            tail_next = tail.next
            curr.next = tail
            curr.next.next = curr_nextt

            curr = curr_nextt
            tail = tail_next
        