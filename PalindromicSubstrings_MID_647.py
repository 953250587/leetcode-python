"""
 Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

    The input string length won't exceed 1000.

"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        246ms
        """
        count = 0
        l = len(s)
        dp = [[False] * l for i in range(l)]
        for i in range(l):
            dp[i][i] = True
            count += 1
            l_1 = min(i, l - i - 1)
            start = i
            end = i
            for k in range(1, l_1 + 1):
                if s[start - 1] == s[end + 1] and dp[start][end]:
                    dp[start - 1][end + 1] = True
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break
            if i +1 < l and s[i] == s[i + 1]:
                dp[i][i + 1] =True
                count += 1
                l_2 = min(i, l - i - 2)
                start = i
                end = i + 1
                for k in range(1, l_2 + 1):
                    if s[start - 1] == s[end + 1] and dp[start][end]:
                        dp[start - 1][end + 1] = True
                        count += 1
                        start -= 1
                        end += 1
                    else:
                        break
        return count

    def countSubstrings_1(self, s):
        """
        :type s: str
        :rtype: int
        169ms
        """
        N = len(s)
        ans = 0
        for center in range(2 * N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

    def countSubstrings_2(self, s):
        """
        :type s: str
        :rtype: int
        39ms
        """
        ans = 0
        start = 0
        while start < len(s):
            end = start
            while end < len(s) and s[start] == s[end]:
                end += 1
            repeat = end - start
            temp = (1 + repeat) * repeat / 2
            left, right = start - 1, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp += 1
                left -= 1
                right += 1

            ans += temp
            start = end

        return ans
print(Solution().countSubstrings('abc'))
print(Solution().countSubstrings('abaaa'))
print(Solution().countSubstrings("aaaaa"))
