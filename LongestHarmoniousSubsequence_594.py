"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

"""
import collections
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        226ms
        """
        unqi=sorted(nums)
        temp=unqi[0]
        count_1=0
        count_2=0
        max_1=0
        for i in unqi:
            if i==temp:
                count_1+=1
            elif i==(temp+1):
                count_2+=1
            else:
                before=temp+1
                temp=i
                if count_1*count_2!=0:
                    max_1=max(count_1+count_2,max_1)
                if before+1==temp:
                    temp=before
                    count_1=count_2
                    count_2=1
                else:
                    count_1=1
                    count_2=0
            print(i,count_1,count_2)
        if count_1 * count_2 != 0:
            max_1 = max(count_1 + count_2, max_1)
        return max_1

    def findLHS_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return max([count[x] + count[x + 1] for x in count if count[x + 1]] or [0])
print(Solution().findLHS([1,1,1,1]))
