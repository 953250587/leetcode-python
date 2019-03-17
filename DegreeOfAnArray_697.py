"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        658ms
        """
        if nums == []:
            return 0
        self.dicts={}
        self.num=0
        self.min_length=-1
        count=0
        for i in nums:
            if i not in self.dicts.keys():
                self.dicts[i]={'start':count,'end':count,'time':1}
            else:
                self.dicts[i]['end']=count
                self.dicts[i]['time']+=1
            self.num=max(self.num,self.dicts[i]['time'])
            count+=1
        for key in self.dicts.keys():
            if self.dicts[key]['time']==self.num:
                if self.min_length==-1:
                    self.min_length=self.dicts[key]['end']-self.dicts[key]['start']+1
                else:
                    self.min_length=min(self.min_length,self.dicts[key]['end']-self.dicts[key]['start']+1)
        return self.min_length

    def findShortestSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        119ms
        """
        if not nums:
            return 0
        m = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in m:
                m[n][1] = i
                m[n][2] += 1
            else:
                m[n] = [i, i, 1]
        l = sorted(m.items(), key=lambda x: x[1][2], reverse=True)
        item = m[l[0][0]]
        pos, c = 0, item[2]
        d = item[1] - item[0] + 1
        while pos < len(l) - 1:
            pos += 1
            item = m[l[pos][0]]
            if item[2] < c:
                break
            d = min(d, item[1] - item[0] + 1)
        return d
print(Solution().findShortestSubArray([1]))

