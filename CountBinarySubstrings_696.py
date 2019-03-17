"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        232ms
        """
        temp=s[0]
        lists=[]
        temp_num=0
        for i in s:
            if i==temp:
                temp_num+=1
            else:
                lists.append(temp_num)
                temp_num=1
            temp=i
        lists.append(temp_num)
        temp=lists[0]
        result=0
        for i in lists[1:]:
            result+=min(temp,i)
            temp=i
        print(lists)
        return result

    def countBinarySubstrings_1(self, s):
        """
        :type s: str
        :rtype: int
        139ms
        """
        n = len(s)
        if n <= 1:
            return 0
        res = 0
        prelen=0
        curlen=0
        cur=s[0]
        for c in s:
            if cur == c:
                curlen += 1
            else:
                prelen = curlen
                curlen = 1
                cur = c
            if prelen >= curlen:
                res += 1
        return res
print(Solution().countBinarySubstrings("00110011"))
print(Solution().countBinarySubstrings("10101"))

