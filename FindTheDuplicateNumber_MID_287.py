"""
 Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        62ms
        """
        low=1
        high=len(nums)-1
        mid=(high+low)//2
        while low<=high:
            count = 0
            for i in nums:
                if i<=mid:
                    count+=1
            if count<=mid:
                low=mid+1
            else:
                high=mid-1
            mid = (high + low) // 2
        return low

    def findDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        35ms
        """
        slow = nums[0]
        fast = nums[nums[0]]
        # 必然存在循环，而且循环开始的为重复数
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        # 如果一格一格移动，则一定会在跳转的时候遇到，否则，slow和fast永不会相等
        # 则就和第一步的2倍相等矛盾
        # 1->3->2->4->5
        #       2<- <-5
        # 如果在第一步在4相遇，则之后fast从0开始，若不再2相遇，则在4相遇，而若是在4相遇
        # 则往前推一步，则在2相遇，矛盾，所以必然在2相遇。其他情况可以以此类推
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
print(Solution().findDuplicate([1,3,4,2,2]))