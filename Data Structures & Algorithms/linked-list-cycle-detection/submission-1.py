# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        slow = head
        fast = head

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow.val == fast.val:
                return True
        
        return False

# [1,2,3,4], 4->2
# slow=1, fast=1
# slow=2, fast=3
# slow=3, fast=2
# slow=4, fast=4, 4==4
# return True

# [1,2,3,4,5]
# slow=1, fast=1
# slow=2, fast=3
# slow=3, fast=5
# return False
