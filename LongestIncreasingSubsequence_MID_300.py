"""
 Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1269ms n^2
        """
        l=len(nums)
        if l<=0:
            return 0
        dp=[0 for i in range(len(nums))]
        dp[-1]=1
        max_1=0
        for i in range(l)[::-1]:
            for j in range(i+1,l):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            if dp[i]==0:
                dp[i]=1
            max_1=max(max_1,dp[i])
            print(dp)
        return max_1

    def lengthOfLIS_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        46ms 有bug
        """
        if not nums:
            return 0

        prev_seq = [nums[0]]
        longest = prev_seq[:]
        for i in range(1, len(nums)):
            # print prev_seq
            # 后备最长增加
            if nums[i] > prev_seq[-1]:
                prev_seq.append(nums[i])
            # 后备最长更替
            elif nums[i] < prev_seq[-1]:
                gti = self.min_gt_k(prev_seq, nums[i])

                prev_seq = prev_seq[:gti] + [nums[i]]

                # if len(new_seq) >= len(prev_seq):
                # prev_seq = new_seq
            # 暂定最长增加
            if nums[i] > longest[-1]:
                longest.append(nums[i])
            # 后备最长代替最长，因为后备的长度已经比原来的长了，而且之后为longest的数一定为
            # prev_seq的数
            if len(longest) < len(prev_seq):
                longest = prev_seq

        return len(longest)

    def min_gt_k(self, nums, k):
        for i in range(len(nums)):
            if nums[i] >= k:
                return i

        return len(nums)
# print(Solution().lengthOfLIS_1([1,2,100,102,103,104,5,6,3,7,8,9,105,106]))
# print(Solution().lengthOfLIS([4,10,4,1,2,3]))
# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

import bisect
class Solution_1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        52ms
        """
        stack=nums[::-1]
        result=[]
        while(stack):
            val=stack.pop()
            if(not result):
                result.append(val)
                print(result)
                continue
            if(val>result[-1]):
                result.append(val)
            else:
                # 把位置一个个替代掉
                temp=bisect.bisect_left(result,val)
                result[temp]=val
            print(result)
        return len(result)

print(Solution_1().lengthOfLIS([1,2,100,102,103,104,5,6,3,7,8,9,105,106]))

