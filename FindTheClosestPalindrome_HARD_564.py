"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:

Input: "123"
Output: "121"

Note:

    The input n is a positive integer represented by string, whose length will not exceed 18.
    If there is a tie, return the smaller one as answer.

"""
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        48MS
        """
        num = int(n)
        L = len(n)
        a = L // 2
        pre = n[:a]
        candidates = []
        if L % 2 == 0:
            num_pre = [str(max(int(pre) - i, 0)) for i in range(-1, 2)]
            str_pre = [i + i[::-1] for i in num_pre]
        else:
            str_pre = [pre + str(max(int(n[a]) + i, 0)) + pre[::-1] for i in range(-1, 2)]
        print(str_pre)
        candidates.extend(str_pre)
        if L > 1:
            candidates.append('9' * (L - 1))
        candidates.append('1' + '0' * (L - 1) + '1')

        min_1 = [num, num]
        for candidate in candidates:
            if candidate != n:
                second = int(candidate)
                diff = abs(second - num)
                if diff < min_1[0]:
                    min_1 = [diff, second]
                elif diff == min_1[0] and second < min_1[1]:
                    min_1 = [diff, second]
        return str(min_1[1])

    def nearestPalindromic_1(self, n):
        """
        :type n: str
        :rtype: str
        70MS
        """
        if len(n) == 1:
            return str(int(n) - 1)

        if len(n) % 2 == 0:
            m = len(n) // 2
        else:
            m = len(n) // 2 + 1

        left = int(n[:m])
        tmp = [str(left + 1), str(left - 1), str(left)]

        sol = []
        for i in tmp:
            sol.append(int(i + ''.join(reversed(i))))
            sol.append(int(i + ''.join(reversed(i[:-1]))))
        sol.append(int('9' * (len(n) - 1)))
        sol.append(int('1' + (len(n) - 1) * '0' + '1'))

        diff = float('inf')
        ans = None
        original = int(n)
        for i in sol:
            if abs(i - original) < diff and abs(i - original) != 0:
                diff = abs(i - original)
                ans = i
            elif abs(i - original) == diff:
                ans = min(i, ans)

        return str(ans)

    def nearestPalindromic_2(self, n):
        """
        :type n: str
        :rtype: str
        43MS
        """
        # based on @awice and @o_sharp
        l = len(n)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))
        # the closest must be in middle digit +1, 0, -1, then flip left to right
        prefix = int(n[:(l + 1) // 2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
# print(Solution().nearestPalindromic('1'))
# print(Solution().nearestPalindromic('9'))
# print(Solution().nearestPalindromic('120'))
# print(Solution().nearestPalindromic("100"))
print(Solution().nearestPalindromic("99"))