class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow

# [1,2,3,2,2]
# [1,2,3,2,2], slow=0->1, fast=0->1->2
# [1,2,3,2,2], slow=1->2, fast=2->3->2, 2==2
# [1,2,3,2,2], slow1=2->3, slow2=0->1
# [1,2,3,2,2], slow1=3->2, slow2=1->2, 2==2
# return 2

# [1,2,3,4,4]
# [1,2,3,4,4], slow=0->1, fast=0->1->2
# [1,2,3,4,4], slow=1->2, fast=2->3->4
# [1,2,3,4,4], slow=2->3, fast=4->4->4
# [1,2,3,4,4], slow=3->4, fast=4->4->4, 4==4
# [1,2,3,4,4], slow1=4->4, slow2=0->1
# [1,2,3,4,4], slow1=4->4, slow2=1->2
# [1,2,3,4,4], slow1=4->4, slow2=2->3
# [1,2,3,4,4], slow1=4->4, slow2=3->4, 4==4
# return 4

# [1,3,4,2,2]
# [1,3,4,2,2], slow=0->1, fast=0->1->3
# [1,3,4,2,2], slow=1->3, fast=3->2->4
# [1,3,4,2,2], slow=3->2, fast=4->2->4
# [1,3,4,2,2], slow=2->4, fast=4->2->4, 4==4
# [1,3,4,2,2], slow1=4->2, slow2=0->1
# [1,3,4,2,2], slow1=2->4, slow2=1->3
# [1,3,4,2,2], slow1=4->2, slow2=3->2, 2==2
# return 2
