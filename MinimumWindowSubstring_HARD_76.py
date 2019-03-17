"""
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        599ms
        """
        import collections
        import heapq
        h = []
        min_len = float('inf')
        result = []
        dicts_len = collections.defaultdict(int)
        dicts = collections.defaultdict(int)
        char_sets = set()
        for char in t:
            dicts_len[char] += 1
            char_sets.add(char)
        def isOk(dicts_len, dicts):
            for key in dicts_len:
                if dicts[key] < dicts_len[key]:
                    return False
            return True

        for i, char in enumerate(s):
            if char in char_sets:
                dicts[char] += 1
                heapq.heappush(h, (i, char))
                if isOk(dicts_len, dicts):
                    end = i
                    while h:
                        c = h[0][1]
                        if dicts[c] - 1 >= dicts_len[c]:
                            heapq.heappop(h)
                            dicts[c] -= 1
                        else:
                            break
                    start = h[0][0]
                    if end - start < min_len:
                        result = [start, end]
                        min_len = end - start
        if result == []:
            return ''
        else:
            return s[result[0]: result[1] + 1]

    def minWindow_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        252ms
        """
        from collections import Counter
        if len(s) < len(t): return ""
        c = Counter(t)
        count = len(t)
        begin = end = 0
        mlen = len(s) + 1
        head = 0
        while end < len(s):
            i = s[end]
            if i in t:
                c[i] -= 1
                if c[i] >= 0: count -= 1
            while count == 0:
                j = s[begin]
                if j in t:
                    c[j] += 1
                    if c[j] > 0:
                        if end - begin + 1 < mlen:
                            mlen = end - begin + 1
                            head = begin
                        count += 1
                begin += 1
            end += 1
        if mlen == len(s) + 1:
            return ""
        return s[head:head + (mlen)]

    def minWindow_2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        132ms
        """
        import sys
        ans = sys.maxint
        start = end = 0
        min_start = 0
        count = len(t)
        dic = [0] * 128
        for c in t:
            dic[ord(c)] += 1

        while end < len(s):
            if dic[ord(s[end])] > 0:
                count -= 1
            dic[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < ans:
                    ans = end - start
                    min_start = start

                dic[ord(s[start])] += 1
                if dic[ord(s[start])] > 0:
                    count += 1
                start += 1

        return "" if ans == sys.maxint else s[min_start:min_start + ans]

    def isValidWindow(self, window, t):
        """
        Return True if `window` covers all characters in t
        """
        tChars = set(list(t))
        for elem in list(window):
            if elem in tChars:
                tChars.remove(elem)

        return len(tChars) == 0

    def minWindow_3(self, s, t):
        """
        115ms
        :param s:
        :param t:
        :return:
        """
        from collections import defaultdict
        minSize = len(s) + 1
        start, end = 0, len(s)
        tCharsCounts = defaultdict(int)
        counter = len(t)

        for elem in list(t):
            tCharsCounts[elem] += 1

        startIdx, endIdx = 0, 0
        while endIdx < len(s):
            endElem = s[endIdx]
            if tCharsCounts[endElem] > 0:
                counter -= 1

            tCharsCounts[endElem] -= 1
            endIdx += 1

            while counter == 0:
                if endIdx - startIdx < minSize:
                    start, end = startIdx, endIdx
                    minSize = endIdx - startIdx

                startElem = s[startIdx]
                tCharsCounts[startElem] += 1
                if tCharsCounts[startElem] > 0:
                    counter += 1

                startIdx += 1

        if minSize == len(s) + 1:
            return ""

        return s[start:start + minSize]
S = "ADOBECODEBANC"
T = "ABC"
print(Solution().minWindow(S, T))
print(Solution().minWindow('adbccadba', 'aabc'))
print(Solution().minWindow('adccbbadbaca', 'aabc'))
print(Solution().minWindow('', 'aabc'))
print(Solution().minWindow("bba", "ab"))


