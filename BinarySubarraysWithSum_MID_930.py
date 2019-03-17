"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?



Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        48 ms
        """
        position = []
        # 找出所有1的位置
        for i, a in enumerate(A):
            if a == 1:
                position.append(i)
        total = 0
        # 针对S=0的情况特别进行讨论
        if S == 0:
            if len(position) == 0:
                return sum([i + 1 for i in range(len(A))])
            for i in range(len(position)):
                between = position[i] - (position[i - 1] + 1 if i > 0 else 0)
                total += sum([i + 1 for i in range(between)])
            between = len(A) - 1 - position[-1]
            total += sum([i + 1 for i in range(between)])
            return total

        for i in range(len(position) - S + 1):
            # 前半段开头包含0的个数，边界需要注意是否越界
            top = position[i] - (position[i - 1] + 1 if i > 0 else 0)
            # 后半段结尾包含0的个数，边界需要注意是否越界
            bottom = (position[i + S] - 1 if i + S < len(position) else len(A) - 1) - position[i + S - 1]
            total += (top + 1) * (bottom + 1)
        return total

    def numSubarraysWithSum_1(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        44ms
        """

        if len(A) == 0:
            return 0

        if sum(A) == 0:
            if S != 0:
                return 0
            return len(A) * (len(A) + 1) / 2

        zero_groups = []
        count = 0
        for elt in A:
            if elt == 1:
                zero_groups.append(count)
                count = 0
            if elt == 0:
                count += 1
        zero_groups.append(count)
        # print zero_groups

        count = 0
        if S == 0:
            for i in range(len(zero_groups)):
                count += (zero_groups[i] * (zero_groups[i] + 1)) / 2
            return count

        for i in range(len(zero_groups) - S):
            count += (zero_groups[i] + 1) * (zero_groups[i + S] + 1)

        return count


print(Solution().numSubarraysWithSum(A = [1,0,1,0,1], S = 2))
print(Solution().numSubarraysWithSum([0,0,0,0,0], 0))
print(Solution().numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0], 0))