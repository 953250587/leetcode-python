"""
 Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        692ms
        """
        def max_(nums1, nums2, k):
            for i in range(k):
                if nums1[i] > nums2[i]:
                    return nums1
                elif nums1[i] < nums2[i]:
                    return nums2
            return nums1

        def join_(nums1, nums2):
            # print('gggg', nums1, nums2)
            # l_1 = len(nums1)
            # l_2 = len(nums2)
            # i, j = 0, 0
            # result = []
            # while i < l_1 and j < l_2:
            #     if nums1[i] > nums2[j]:
            #         result.append(nums1[i])
            #         i += 1
            #     elif nums1[i] < nums2[j]:
            #         result.append(nums2[j])
            #         j += 1
            #     else:
            #         i_copy = i + 1
            #         j_copy = j + 1
            #         while i_copy < l_1 and j_copy < l_2:
            #             if nums1[i_copy] > nums2[j_copy]:
            #                 result.append(nums1[i])
            #                 i += 1
            #                 break
            #             elif nums1[i_copy] < nums2[j_copy]:
            #                 result.append(nums2[j])
            #                 j += 1
            #                 break
            #             else:
            #                 i_copy += 1
            #                 j_copy += 1
            #         if i_copy <= l_1 and j_copy >= l_2:
            #             result.append(nums1[i])
            #             i += 1
            #         elif i_copy >= l_1 and j_copy < l_2:
            #             result.append(nums2[j])
            #             j += 1
            # if i < l_1:
            #     result += nums1[i:]
            # else:
            #     result += nums2[j:]
            # return result
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans


        def find_max(lists, k):
            l = len(lists)
            k = min(k, l)
            result = []
            i = 0
            while i < l:
                a = lists[i]
                while result and result[-1] < a and l - i > k:
                    result.pop()
                    k += 1
                if k > 0:
                    result.append(a)
                    k -= 1
                i += 1
            return result
        l_1 = len(nums1)
        l_2 = len(nums2)
        p = [i for i in range(min(l_1, k) + 1)]
        p_ans = []
        a = nums1
        for i in p[::-1]:
            a = find_max(a, i)
            p_ans.append(a)
        print(p_ans)
        q = [i for i in range(min(l_2, k) + 1)]
        a = nums2
        q_ans = []
        for i in q[::-1]:
            a = find_max(a, i)
            q_ans.append(a)
        print(q_ans)
        ans = [0] * k
        for i in p:
            a = k - i
            if a in set(q):
                ans = max_(ans, join_(p_ans[-i - 1], q_ans[-a - 1]), k)
                # print('ggg', p_ans[-i - 1], q_ans[-a - 1])
            # print(i, a, ans)
        return ans

        # print(find_max(nums1, 3))
        # print(find_max(nums1, 4))

    def maxNumber_1(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        505ms
        """

        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))

    def maxNumber_2(self, a, b, k):
        """
        149ms
        :param a: 
        :param b: 
        :param k: 
        :return: 
        """""
        lena = len(a)
        lenb = len(b)

        def fill(a, c):
            last = [-1] * 10
            for i, v in enumerate(a):
                c[v][last[v] + 1:i + 1] = [i] * (i - last[v])
                last[v] = i

        if k <= (lena + lenb) * 5 / 6:
            N = 100
            if lena >= N:
                c = [[None] * lena for i in range(10)]
                fill(a, c)
            else:
                c = None

            if lenb >= N:
                d = [[None] * lenb for i in range(10)]
                fill(b, d)
            else:
                d = None
        else:
            c = None
            d = None

        def maxd(a, i, b, j, k, c):
            ln1 = len(a) - i
            n1 = ln1 - (k - len(b) + j) + 1
            n1 = min(ln1, n1)
            if n1 == 1:
                return 0, a[i]

            if c is None or (n1 <= 5):
                i0 = i
                nums = a[i0:i0 + n1]

                m = max(nums)
                i = nums.index(m)
                m1 = i, m
                return m1

            for d in range(9, -1, -1):
                dn = c[d][i]
                if dn is None:
                    continue
                r = dn - i
                if r < n1:
                    ret = r, d
                    break

            return ret

        ret = []
        s = set()
        s.add((0, 0))
        while k > 0:
            m = -1
            ss = [None for _ in range(10)]
            for i, j in s:
                if i < lena:
                    m1 = maxd(a, i, b, j, k, c)
                    if m1 and m1[1] >= m:
                        m = m1[1]
                        if ss[m] is None:
                            ss[m] = set()
                        new_i = i + m1[0] + 1
                        #                        if new_i > len(a):
                        #                            print('vvv')
                        ss[m].add((new_i, j))
                if j < lenb:
                    m2 = maxd(b, j, a, i, k, d)
                    if m2 and m2[1] >= m:
                        m = m2[1]
                        if ss[m] is None:
                            ss[m] = set()
                        ss[m].add((i, j + m2[0] + 1))

            ret.append(m)
            s = ss[m]  # set([x for x in d if d[x] == m])
            k -= 1
        return ret

print(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
print(Solution().maxNumber([6, 7], [6, 0, 4], 5))
print(Solution().maxNumber([3, 9], [8, 9], 3))
print(Solution().maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2],15))
print(Solution().maxNumber([5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3],[7,6,7,1,0,1,0,5,6,0,5,0],31))
print(Solution().maxNumber([4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2],[9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3],60))