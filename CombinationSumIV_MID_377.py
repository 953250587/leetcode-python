"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.targets=[0 for i in range(target+1)]
        self.new_nums=[0]
        while self.new_nums!=[]:
            self.nums=[]
            for i in self.new_nums:
                for j in nums:
                    a=i+j
                    if a<=target:
                        self.nums.append(a)
                        self.targets[a]+=1
            self.new_nums=self.nums
        return self.targets[target]

    def combinationSum4_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        52ms
        """
        self.targets=[0 for i in range(target+1)]
        self.targets[0]=1
        for i in range(1,target+1):
            for j in nums:
                if i-j>=0:
                    self.targets[i]+=self.targets[i-j]
        print(self.targets)
        return self.targets[target]

    def combinationSum4_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        55ms
        """
        DP = [0 for _ in range(target + 1)]
        DP[0] = 1
        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    DP[i] = DP[i] + DP[i - j]
        return DP[-1]


nums = [1]
target = 4
# nums=[1,2,3]
# target=4
print(Solution().combinationSum4_1(nums,target))
