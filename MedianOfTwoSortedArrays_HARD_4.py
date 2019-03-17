"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        188ms
        """
        m = len(nums1)
        n = len(nums2)
        if m == n == 1:
            return (nums1[0] + nums2[0]) / 2
        k = (m + n + 1) // 2
        a = min(m, n)
        if m > n:
            nums1, nums2 = nums2, nums1
        if nums1 == []:
            m = len(nums2)
            if m % 2 == 1:
                return nums2[m // 2] / 1
            else:
                return (nums2[m // 2 - 1] + nums2[m // 2]) / 2
        high = a - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if mid + 1 > k:
                high = mid - 1
                continue
            if mid + 1 + len(nums2) < k:
                low = mid + 1
                continue
            if k - mid - 2 < 0 or nums1[mid] >= nums2[k - mid - 2]:
                flag = 'left'
                left_max = nums1[mid]
                if mid + 1 < a:
                    right_min = min(nums2[k - mid - 1], nums1[mid + 1])
                else:
                    right_min = nums2[k - mid - 1]
            else:
                flag = 'right'
                left_max = nums2[k - mid - 2]
                if mid + 1 < a:
                    right_min = min(nums2[k - mid - 1], nums1[mid + 1])
                else:
                    right_min = nums2[k - mid - 1]
            print(flag)
            if left_max <= right_min:
                if (m + n) % 2 == 1:
                    return left_max / 1
                else:
                    return (left_max + right_min) / 2
            else:
                if flag == 'left':
                    high = mid - 1
                else:
                    low = mid + 1
        if (m + n) % 2 == 1:
            return nums2[k - 1] / 1
        else:
            if k >= len(nums2):
                return (nums2[k - 1] + nums1[0]) / 2
            else:
                return (nums2[k - 1] + min(nums2[k], nums1[0])) / 2

    def findMedianSortedArrays_1(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        96MS
        """
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)

    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        128ms
        """

        # 1.  get len of list
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        # 2. init
        imin, imax, half_len = 0, m, (m + n + 1) / 2

        # loop
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i

            # judge
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [-1, 0 ,1, 2, 5]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1, 3]
nums2 = []
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [0, 3, 4, 6, 8]
nums2 = [1, 2, 5, 7]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [0, 3, 4, 6, 9]
nums2 = [1, 2, 5, 7, 8]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [6, 7, 8]
nums2 = [0, 1, 2, 3, 4, 5]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1]
nums2 = [2,3]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [3, 4]
nums2 = [0, 1, 2, 5]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1, 1]
nums2 = [1, 2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [1, 1]
print(Solution().findMedianSortedArrays(nums1, nums2))