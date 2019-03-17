"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        332ms
        """
        import heapq, collections
        h = []
        dict = collections.defaultdict(int)
        for i in range(k - 1):
            heapq.heappush(h, -nums[i])
            dict[-nums[i]] += 1
        result = []
        for i, num in enumerate(nums[k - 1: ]):
            heapq.heappush(h, -num)
            dict[-num] += 1
            result.append(-h[0])
            dict[-nums[i]] -= 1
            if dict[-nums[i]] == 0:
                del dict[-nums[i]]
            while h and h[0] not in dict:
                heapq.heappop(h)
            # print(dict)
            # print(h)
        return result

    def maxSlidingWindow_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        256ms
        """
        import collections
        # so the basic idea is to maintain a queue as a buffer to store the indices
        # the indices will be increasing while the corresponded elements will be decreasing
        # we ensure this by pop up the tail element when it is smaller than the current num[i]
        # by doing this, we access the head to find the maximum for current window [i-k+1, i]
        ret = []
        dq = collections.deque()
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            # now lets push this
            dq.append(i)
            if dq[0] == i - k:
                # need to pop this because next time it cannot be counted anymore
                dq.popleft()
            if i >= k - 1:
                # the window is full now
                ret.append(nums[dq[0]])
        return ret

    def maxSlidingWindow_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        185ms
        """
        if not nums: return []
        maxcarry = max(nums[:k])
        store = [maxcarry]
        for i in range(k, len(nums)):
            if maxcarry != nums[i - k]:
                maxcarry = max(maxcarry, nums[i])
            else:
                maxcarry = max(nums[(i - k + 1):(i + 1)])
            store.append(maxcarry)
        return store
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

nums = [1,3,1,2,0,5]
k = 3
print(Solution().maxSlidingWindow(nums, k))

