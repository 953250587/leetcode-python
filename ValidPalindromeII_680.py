"""
 Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        198ms
        """
        l=len(s)
        for i in range(l//2):
            if s[i]!=s[l-i-1]:
                new_s=s[:i]+s[i+1:]
                new_s_2=s[:l-i-1]+s[l-i:]
                return new_s==new_s[::-1] or new_s_2==new_s_2[::-1]
        return True

    def validPalindrome_1(self, s):
        # 206ms
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
print(Solution().validPalindrome('abcdbca'))