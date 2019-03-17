"""
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:

Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Note:

    2 <= len(nums) <= 10000.
    0 <= nums[i] < 1000000.
    1 <= k <= len(nums) * (len(nums) - 1) / 2.

"""


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        import heapq
        import bisect
        # nums = sorted(nums)
        c = collections.Counter(nums)
        nums = []
        for i in c:
            bisect.insort_left(nums, (i, c[i]))
        l = len(nums)
        h = []
        print('nums', nums)
        for i in range(l):
            heapq.heappush(h, (0, i, i, nums[i][1] * (nums[i][1] - 1) // 2))
        while k > 0:
            a = heapq.heappop(h)
            if a[2] < l - 1:
                heapq.heappush(h, (abs(nums[a[2] + 1][0] - nums[a[1]][0]), a[1], a[2] + 1, nums[a[2] + 1][1] * nums[a[1]][1]))
            k -= a[-1]
            print(k, a)
        return a[0]


    def smallestDistancePair_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        191ms
        """
        import bisect
        nums = sorted(nums)
        max_range = nums[-1] - nums[0]
        low, high = 0, max_range

        while low < high:
            mid = (low + high) // 2
            used = {}
            counts = 0
            for i, num in enumerate(nums):
                if num in used:
                    counts += used[num] - i - 1
                else:
                    count = bisect.bisect_right(nums, num + mid)
                    used[num] = count
                    counts += count - i - 1
            if counts < k:
                low = mid + 1
            else:
                high = mid
            print('mid',mid, 'counts', counts, 'K', k)
        return low

    def smallestDistancePair_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        96ms
        """
        n = len(nums)
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (high - low) / 2 + low
            guess = 0
            i = 0
            for j in range(1, n):
                while nums[j] - nums[i] > mid:
                    i += 1
                guess += j - i
            if guess < k:
                low = mid + 1
            else:
                high = mid
        return low
# print(Solution().smallestDistancePair_1(nums = [1,3,1], k = 1))
# print(Solution().smallestDistancePair_1(nums = [1,3,2,4,7], k = 10))
# print(Solution().smallestDistancePair_1([0,0,0,0,0,1,1,1,1,1,2,2,2,2], 20))
print(Solution().smallestDistancePair_1([62,100,4], 2))