"""
 Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

    The length of the given array will not exceed 15.
    The range of integer in the given array is [-100,100].
    The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

"""
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1212ms
        """
        self.nums = nums
        self.one=set()
        self.result = set()
        def dfs(position):
            if position >= len(self.nums):
                return
            b = set()
            for j in self.one:
                if j <= self.nums[position]:
                    b.add((j, self.nums[position]))
            for i in self.result:
                if i[-1] <= self.nums[position]:
                    b.add(tuple(list(i) + [self.nums[position]]))
            self.one.add(self.nums[position])
            for j in b:
                self.result.add(j)
            dfs(position + 1)
        dfs(0)
        self.result = list(self.result)
        count = 0
        if len(self.result) <= 0:
            return []
        while type(self.result[count]) == tuple:
            a = self.result[count]
            self.result.remove(a)
            self.result.append(list(a))

        return self.result

    def findSubsequences_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        705ms
        """
        self.res = []
        used = set()
        for x in range(len(nums) - 1):
            if nums[x] not in used:
                self.dfs(nums, x, [nums[x]])
                used.add(nums[x])
        return self.res

    def dfs(self, nums, index, current):
        if len(current) >= 2:
            self.res += [current]
        used = set()
        for x in range(index + 1, len(nums)):
            if nums[x] not in used and nums[x] >= current[-1]:
                self.dfs(nums, x, current + [nums[x]])
            used.add(nums[x])

# a = set()
# b = set()
# a.add((1, 2))
# a.add((3, 4))
# for i in a:
#     print(i)
#     b.add(tuple(list(i) + [1]))
# for i in b:
#     a.add(i)
# print(a)
print(Solution().findSubsequences([4, 3, 2, 1]))

