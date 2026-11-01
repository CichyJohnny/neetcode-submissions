# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        i = 0
        while curr:
            curr = curr.next
            i += 1
        
        curr = l2
        j = 0
        while curr:
            curr = curr.next
            j += 1
        
        if i < j:
            l1, l2 = l2, l1
        
        prev = None
        l1_curr = l1
        l2_curr = l2
        
        carry_over = 0
        while l2_curr:
            print(l1_curr.val, l2_curr.val, carry_over)
            val = l1_curr.val + l2_curr.val + carry_over
            l1_curr.val = val % 10
            carry_over = val // 10

            prev = l1_curr
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
        
        while l1_curr and carry_over:
            val = l1_curr.val + carry_over
            l1_curr.val = val % 10
            carry_over = val // 10

            prev = l1_curr
            l1_curr = l1_curr.next
        
        l1_curr = prev
        if carry_over > 0:
            l1_curr.next = ListNode(carry_over)

        return l1


# l1=[7,8,9], l2=[6,7,8,9]
# l1=[7,8,9], l2=[6,7,8,9], i=3, j=4
# l1=[6,7,8,9], l2=[7,8,9], i=3, j=4
# l1=[6,4,8,9], l2=[7,8,9], carry_over=1
# l1=[6,4,7,9], l2=[7,8,9], carry_over=1
# l1=[6,4,7,9], l2=[7,8,9], carry_over=1, 1>0
# l1=[6,4,7,9,1], l2=[7,8,9], carry_over=1, 1>0