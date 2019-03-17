"""
 Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        49ms
        """
        c=[0 for i in range(26)]
        for C in s:
            c[ord(C)-ord('a')]+=1
        self.sets=set()
        for i in range(26):
            if c[i]>=k:
                self.sets.add(i)
        self.sum=0
        start=0
        flag=False

        def max_long(s,k):
            if len(s)<k:
                return
            c = set()
            num=[0 for i in range(26)]
            for i in s:
                c.add(i)
                num[ord(i)-ord('a')]+=1
            sets = set()
            for i in c:
                if num[ord(i)-ord('a')] <k:
                    sets.add(i)
            if len(sets)==0:
                self.sum=max(self.sum,len(s))
                return
            ALL=[s]
            while len(sets)>0:
                a=[]
                b=sets.pop()
                for i in ALL:
                    a.extend(i.split(b))
                ALL=a
            for i in ALL:
                max_long(i,k)

        for i in range(len(s)):
            if ord(s[i])-ord('a') in self.sets:
                flag=True
            else:
                if flag:
                    sub=s[start:i]
                    max_long(sub,k)
                    flag = False
                start=i
        if flag:
            sub = s[start:len(s)]
            max_long(sub, k)
        return self.sum

    def longestSubstring_1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        59ms
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

s = "bbaaacbd"
k = 3
# s = "ababacb"
# k = 3
# s='aaabbb'
# k=3
# s="aabcabb"
# k=3
print(Solution().longestSubstring(s,k))
