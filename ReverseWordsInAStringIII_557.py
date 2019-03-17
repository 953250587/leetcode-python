"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        126ms
        """
        long=s.split(' ')
        b=''
        for a in long:
            b+=a[::-1]
            b+=' '
        return b.rstrip()

        # return ' '.join(word[::-1] for word in s.split(' ')) 49ms
print(Solution().reverseWords("Let's take LeetCode contest"))