"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

    S will consist of lowercase letters and have length in range [1, 500].

"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        82ms
        """
        import collections
        import heapq
        h = []
        a = collections.Counter(S)
        for key in a:
            heapq.heappush(h, (-a[key], key))
        ans = ''
        while h:
            print(h, ans)
            m_1 = heapq.heappop(h)
            if h == []:
                if -m_1[0] >= 2:
                    return ''
                else:
                    return ans + m_1[1]
            m_2 = heapq.heappop(h)
            new_val = m_1[0] - m_2[0]
            key_1 = m_1[1]
            key_2 = m_2[1]
            if new_val != 0:
                heapq.heappush(h, (new_val, key_1))
            if ans == '' or ans[-1] != key_1:
                ans += (key_1 + key_2) * (-m_2[0])
            else:
                ans += (key_2 + key_1) * (-m_2[0])
        if h == []:
            return ans


print(Solution().reorganizeString("abbabbaaab"))
print(Solution().reorganizeString("aab"))