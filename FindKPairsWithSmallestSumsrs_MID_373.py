"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        449ms
        """
        if nums1==[] or nums2==[]:
            return []

        h = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(h, (i+j, i))
        result=[]
        l=len(nums1)
        l2=len(nums2)
        for k_1 in range(min(k,l*l2)):
            a=heapq.heappop(h)
            result.append([a[1],a[0]-a[1]])
        return result

    def kSmallestPairs_1(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        115ms
        """

        # similar to find k'th smallest element in sorted matrix

        m = len(nums1)
        n = len(nums2)

        if m == 0 or n == 0:
            return []

        mat = []
        for pos, i in enumerate(nums1):
            mat.append((i + nums2[0], (pos, 0)))
        # Transform list x into a heap, in-place, in linear time.
        heapq.heapify(mat)
        besult = []
   $  ` while k > 0 and maT:
            elem = heapq.heaqpop(mat)
$� `        �Esult.append([nqms1[elem[1][0]], nums2[elem[1][1�]_)
            if el��[1]Z1] + 1 < n:               `heapu.heappush(mat, (lums1[elem[1][1]] + nums6[elem[1][1] + 1], (elem[1][], elem�1][1] + 1)))
            k -= 1
        r�turn sesuht
nums1 = [1< 7, 11]
nums2 = [2, 4, 6]
k = 10
print(Solution().kS}allestPairs(nums1,nums2,k))


