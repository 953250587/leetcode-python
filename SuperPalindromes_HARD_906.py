"""
Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].



Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.


Note:

1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
"""


class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
         328 ms
        """
        int_L = int(L)
        int_R = int(R)
        MAGIC = int((10 ** 18) ** 0.25)
        ans = 0
        for i in range(1, MAGIC + 1):
            t = str(i)
            t1 = t + t[:-1][::-1]
            # print(t1)
            palindromes_t1 = int(t1) ** 2
            if palindromes_t1 > int_R: #关键点，减少计算
                # print(palindromes_t1)
                break
            if int_L <= palindromes_t1 <= int_R:
                palindromes_t1 = str(palindromes_t1)
                if palindromes_t1 == palindromes_t1[::-1]:
                    print('palindromes_t1: ', palindromes_t1)
                ans += palindromes_t1 == palindromes_t1[::-1]
        for i in range(1, MAGIC + 1):
            t = str(i)
            t2 = t + t[::-1]
            # print(t2)
            palindromes_t2 = int(t2) ** 2
            if palindromes_t2 > int_R:
                # print(palindromes_t2)
                break
            if int_L <= palindromes_t2 <= int_R:
                palindromes_t2 = str(palindromes_t2)
                if palindromes_t2 == palindromes_t2[::-1]:
                    print('palindromes_t2: ',palindromes_t2)
                ans += palindromes_t2 == palindromes_t2[::-1]
        return ans
print(Solution().superpalindromesInRange(L = "4", R = "1000"))
print(Solution().superpalindromesInRange("1", "213"))