"""
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

Note:

    The length of the input is in range of [1, 10000]

"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        779ms
        """
        import heapq
        seqs = {num: [] for num in nums}
        for num in nums:
            shortest_seq = 0
            if num - 1 in seqs and len(seqs[num - 1]):
                shortest_seq = heapq.heappop(seqs[num - 1])
            heapq.heappush(seqs[num], shortest_seq + 1)
        return len([None for seq_lengths in seqs.values() if len(seq_lengths) and seq_lengths[0] < 3]) == 0

    def isPossible_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        139ms
        """
        '''
        First, let's break up the problem into groups based on if elements are adjacent. These are disjoint subproblems that don't interfere with each other since each subsequence cannot be in more than one group, so we can solve them separately.

Now, for each group of consecutive elements, we'll work with how many copies of each element there is. For example, if we have [1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7], then the copies are chunk = [1, 1, 2, 3, 1, 1, 2].

The key idea is: if we go from say, two copies of 10 to five copies of 11, we know that 3 subsequences must have started at 11. Similarly, if we go from five copies of 11 to three copies of 12, we know that 2 subsequences must have ended at 11.

Now knowing the start and ending positions of every subsequence, let's try to pair the k-th starting position with the k-th ending position. This will make the minimum sized subsequence as long as possible. If they are all legal subsequences, it's possible; otherwise, it's impossible.

Note that this solution can easily be modified to change the minimum of K = 3 to any minimum, by changing s+2. Also note that in the above argument, there could have been more starting and ending positions, but adding more will only make some subsequences smaller, so we don't need to consider those cases.
        '''
        import itertools
        A = nums
        counts = [(x, len(list(group)))
                  for x, group in itertools.groupby(A)]

        def possible(chunk):
            starts, ends = [], []
            prev_count = 0
            for time, count in enumerate(chunk):
                if count > prev_count:
                    starts.extend([time] * (count - prev_count))
                elif count < prev_count:
                    ends.extend([time - 1] * (prev_count - count))
                prev_count = count

            ends.extend([time] * count)
            return all(e >= s + 2 for s, e in zip(starts, ends))

        chunk = []
        prev = None
        for x, count in counts:
            if prev is None or x - prev == 1:
                chunk.append(count)
            else:
                if not possible(chunk):
                    return False
                chunk = []
            prev = x

        return possible(chunk)

    def isPossible_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        86ms
        """
        size = len(nums)
        if size < 3:
            return False
        p1, p2, p3 = 0, 0, 0
        c1, c2, c3 = 0, 0, 0
        pre = nums[0] - 2
        cur = nums[0]
        cnt = 0
        nums.append(nums[0] - 1)
        for num in nums:
            if cur == num:
                cnt += 1
                continue
            if cur == pre + 1:
                if cnt < p1 + p2:
                    return False
                else:
                    c1 = 0
                    if cnt > p1 + p2 + p3:
                        c1 = cnt - p1 - p2 - p3
                    c2 = p1
                    c3 = p2
                    if cnt - p1 - p2 > p3:
                        c3 += p3
                    else:
                        c3 += cnt - p1 - p2
                        # c1, c2, c3 = max(0, cnt - p1 - p2 - p3), p1, min(cnt - p1, p2 + p3)
            else:
                if p1 != 0 or p2 != 0:
                    return False
                else:
                    c1, c2, c3 = cnt, 0, 0
            pre, p1, p2, p3 = cur, c1, c2, c3
            cur = num
            cnt = 1

        if p1 == 0 and p2 == 0:
            return True
        else:
            return False
print(Solution().isPossible([1,2,3,3,4,5]))
print(Solution().isPossible([1,2,3,3,4,4,5,5]))
print(Solution().isPossible([1,2,3,4,4,5]))
print(Solution().isPossible([1,2,3]))
print(Solution().isPossible([]))
print(Solution().isPossible([1]))
print(Solution().isPossible([1,2,2,3,3,4,4,5]))