"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        449ms
        """
        l=0
        result=[]
        while l<len(nums):
            print(nums)
            if nums[l]!=l+1:
                if nums[nums[l]-1]==-1:
                    nums[nums[l]-1]=nums[l]
                    nums[l]=-1
                    l+=1
                elif nums[nums[l]-1]==nums[l]:
                    result.append(nums[l])
                    nums[l] = -1
                    l += 1
                else:
                    nums[nums[l] - 1],nums[l]=nums[l],nums[nums[l] - 1]
            else:
                l+=1
        return result

    def findDuplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        365ms
        """
        res = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                res.append(abs(i))
            else:
                nums[index] = -1 * nums[index]
        return res
nums=[4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))
nums=[2,2]
print(Solution().findDuplicates(nums))
