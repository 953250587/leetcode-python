"""
 Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
"""
import bisect
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        245ms
        """
        l = len(arr)
        pos = bisect.bisect_left(arr, x)
        # if pos >= l:
        #     result = [arr[-i] for i in range(k, 0, -1)]
        #     return result
        if pos > 0:
            start = pos - 1
        else:
            start = 0
        end = start + 1
        while k > 0:
            print(start, end)
            if end == l or (start >= 0 and x - arr[start] <= arr[end] - x):
                start -= 1
            else:
                end += 1
            k -= 1
        result = [arr[i] for i in range(start + 1, end)]
        return result

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        218ms
        """
        n = len(arr)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if mid + k >= n or abs(arr[mid] - x) <= abs(arr[mid + k] - x):
                hi = mid
            else:
                lo = mid + 1
        return arr[lo:lo + k]

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        222ms
        """
        low = 0
        high = len(arr) - k
        while low < high:
            mid = (low + high) // 2
            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                low = mid + 1
            else:
                high = mid
        return arr[low:low + k]
print(Solution().findClosestElements([1,2,3,4,5], k=4, x=3))
print(Solution().findClosestElements([1,2,3,4,5], k=4, x=-1))
print(Solution().findClosestElements([1,2,3,4,5], k=4, x=5))
print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))

