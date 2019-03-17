"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        39ms
        """
        nums=sorted(nums)
        count=0
        i=0
        j=len(nums)-1
        while i<=j:
            count+=nums[j]-nums[i]
            i+=1
            j-=1
        return count
nums=[1,2]
print(Solution().minMoves2(nums))
nums=[1,2,4]
print(Solution().minMoves2(nums))
nums=[1,2,5]
print(Solution().minMoves2(nums))