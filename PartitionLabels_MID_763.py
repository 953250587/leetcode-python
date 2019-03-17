"""
 A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        54ms
        """
        l = len(S)
        dicts = {}
        for i in range(l - 1, -1, -1):
            key = S[i]
            if key not in dicts:
                dicts[key] = i
        end = -1
        start = -1
        result = []
        for i,char in enumerate(S):
            end = max(end, dicts[char])
            if i == end:
                result.append(end - start)
                start = i
        return result
print(Solution().partitionLabels(S = "ababcbacadefegdehijhklij"))
print(Solution().partitionLabels(''))

