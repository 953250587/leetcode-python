"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        20ms
        """
        return str.lower()

        # return ''.join([chr(ord(c) + 32) if ord(c) >= 65 and ord(c) <= 90 else c for c in str])