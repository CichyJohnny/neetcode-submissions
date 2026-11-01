"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        l = dict()

        new = Node(0)
        curr_new = new
        curr_old = head
        while curr_old:
            curr_new.val = curr_old.val

            l[curr_old] = curr_new
            
            curr_old = curr_old.next

            curr_new.next = Node(0) if curr_old else None
            curr_new = curr_new.next
        
        curr = new
        curr_new = new
        curr_old = head
        while curr_old:
            if curr_old.random:
                curr_new.random = l[curr_old.random]

            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return new
