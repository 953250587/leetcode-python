"""
 Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:

Input: N = 10
Output: 9

Example 2:

Input: N = 1234
Output: 1234

Example 3:

Input: N = 332
Output: 299

Note: N is an integer in the range [0, 10^9].
"""
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        36ms
        """
        S = str(N)
        temp = ord(S[0])
        flag = True
        for i, char in enumerate(S):
            if ord(char) < temp:
                flag = False
                flag_val = temp
                break
            temp = ord(char)
        if flag:
            return N
        ans = 0
        for k in range(len(S)):
            if ord(S[k]) < flag_val:
                ans += int(S[k])
            elif ord(S[k]) == flag_val:
                ans += int(S[k]) - 1
                break
            ans *= 10
        print(k)
        for p in range(k + 1, len(S)):
            ans *= 10
            ans += 9
        return ans
print(Solution().monotoneIncreasingDigits(10))
print(Solution().monotoneIncreasingDigits(1234))
print(Solution().monotoneIncreasingDigits(332))
print(Solution().monotoneIncreasingDigits(12344))
print(Solution().monotoneIncreasingDigits(1234321))
