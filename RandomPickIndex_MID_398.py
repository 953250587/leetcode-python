"""
 Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

"""

import random
class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        96ms
        """
        self.nums=nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        list=[]
        count=0
        for i in self.nums:
            if i==target:
                list.append(count)
            count+=1
        l=len(list)
        a=random.randint(0,l-1)
        return list[a]
        # 95ms
        # return random.choice([k for k, v in enumerate(self.nums) if v == target])


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)
nums = [1,2,3,3,3]
solution = Solution(nums)
for i in range(20):
    print(solution.pick(3))
print(solution.pick(1))