"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        398ms
        """
        if nums == []:
            return []
        nums=sorted(nums)
        l=len(nums)
        self.sets=set()
        self.dp={}
        self.dp_num = {}
        self.max=0
        self.max_num=0
        for i in range(l):
            self.dp[nums[i]]=1
            for j in nums[:i]:
                if nums[i]%j==0:
                    if self.dp[nums[i]]<self.dp[j]+1:
                        self.dp[nums[i]]=self.dp[j]+1
                        self.dp_num[nums[i]]=j
            if self.max<self.dp[nums[i]]:
                self.max=self.dp[nums[i]]
                self.max_num=nums[i]

        temp=self.max_num
        result=[]
        self.sets=set(self.dp_num.keys())
        while temp !=None:
            result.append(temp)
            if temp in self.sets:
                temp=self.dp_num[temp]
            else:
                temp=None
        return result

    def largestDivisibleSubset_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()

        def getFactors(n):
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    yield i
                    if n // i != i: yield n // i

        max_len = 0
        answer = []
        d = {}
        for i in nums:
            d[i] = [i]
            for factor in getFactors(i):
                if factor in d and factor != i and 1 + len(d[factor]) > len(d[i]):
                    d[i] = d[factor] + [i]
            if len(d[i]) > max_len:
                max_len = len(d[i])
                answer = d[i]
        return answer

nums=[1,2,4,8]
print(Solution().largestDivisibleSubset(nums))