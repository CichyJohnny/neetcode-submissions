# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            elif list1:
                curr.next = list1
                list1 = list1.next
            elif list2:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = None
        return head.next