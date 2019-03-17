"""
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        39ms
        """
        max_1 = 0
        sets = set(nums)
        while sets:
            count = 1
            a = list(sets)[0]
            sets.remove(a)
            i = a - 1
            while sets and i in sets:
                sets.remove(i)
                count += 1
                i -= 1
            j = a + 1
            while sets and j in sets:
                sets.remove(j)
                count += 1
                j += 1
            max_1 = max(max_1, count)
        return max_1

    def longestConsecutive_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        35ms
        """
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                x = n + 1
                while x in nums:
                    x += 1
                res = max(res, x - n)
        return res

    def longestConsecutive_2(self, nums):
        """
        35ms
        :param nums:
        :return:
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([i for i in range(1000)]))




