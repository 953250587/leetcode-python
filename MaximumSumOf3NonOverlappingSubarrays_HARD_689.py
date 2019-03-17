"""
 In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        118ms
        """
        l = len(nums)
        def dp_last_(nums):
            # print('num', nums)
            dp_last = [-1] * l
            last = sum(nums[0: k])
            max_last = last
            dp_last[k - 1] = [0, last]
            for i in range(k, l - 2 * k):
                last += nums[i] - nums[i - k]
                if last > max_last:
                    max_last = last
                    dp_last[i] = [i - k + 1, last]
                else:
                    dp_last[i] = dp_last[i - 1]
                # print('max', max_last)
            return dp_last

        def dp_start_(nums):
            # print('num', nums)
            dp_last = [-1] * l
            last = sum(nums[0: k])
            max_last = last
            dp_last[k - 1] = [0, last]
            for i in range(k, l - 2 * k):
                last += nums[i] - nums[i - k]
                if last >= max_last:
                    max_last = last
                    dp_last[i] = [i - k + 1, last]
                else:
                    dp_last[i] = dp_last[i - 1]
                # print('max', max_last)
            return dp_last[::-1]
        dp_last = dp_last_(nums)
        print(dp_last)
        dp_start = dp_start_(nums[::-1])
        print(dp_start)
        m_part = sum(nums[k : 2 * k])
        m = m_part + dp_last[k - 1][1] + dp_start[2 * k][1]
        m_recom = [dp_last[k - 1][0], k, l - dp_start[2 * k][0] - k]
        for i in range(2 * k, l - k):
            m_part += nums[i] - nums[i - k]
            m_cur = m_part + dp_last[i - k][1] + dp_start[i + 1][1]
            if m_cur > m:
                m = m_cur
                m_recom = [dp_last[i - k][0], i - k + 1, l - dp_start[i + 1][0] - k]
        return m_recom

    def maxSumOfThreeSubarrays_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        103ms
        """
        n = len(nums)
        ss = [0] * (n + 1)
        for i in range(1, n + 1):
            ss[i] = ss[i - 1] + nums[i - 1]

        left = [0] * (n - 2 * k);
        right = [n - k] * (n)
        for i in range(k, n - 2 * k):
            pre = left[i - 1]
            if ss[i + 1] - ss[i + 1 - k] > ss[pre + k] - ss[pre]:
                left[i] = i - k + 1
            else:
                left[i] = pre

        for i in range(n - k - 1, 2 * k - 1, -1):
            pre = right[i + 1]
            if ss[i + k] - ss[i] >= ss[pre + k] - ss[pre]:
                right[i] = i
            else:
                right[i] = pre

        ans = [n, n, n];
        maxx = -2 ** 31

        for i in range(k, n - 2 * k + 1):
            l = left[i - 1];
            r = right[i + k]
            if ss[i + k] - ss[i] + ss[l + k] - ss[l] + ss[r + k] - ss[r] > maxx:
                ans = [l, i, r]
                maxx = ss[i + k] - ss[i] + ss[l + k] - ss[l] + ss[r + k] - ss[r]
        return ans

    def maxSumOfThreeSubarrays_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        80ms
        """
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k * 2]

        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k * 2])
        seqThreeSum = sum(nums[k * 2:k * 3])

        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1
        while threeSeqIndex <= len(nums) - k:
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1
        return bestThreeSeq


print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))

