"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

    S will be a string with length at most 12.
    S will consist only of letters or digits.

"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        131ms
        """
        # 记录当前所有的分支
        cur_s = [S]
        # 每次都从上一轮记录的位置的下一位开始计算
        for i in range(len(S)):
            next_s = []
            for s in cur_s:
                # 如果是数字，则当前分支直接加入下轮的分支
                if s[i].isdigit():
                    next_s.append(s)
                # 如果是字母，则当前分支分为大小写两种加入下轮的分支
                else:
                    next_s.append(s[0:i] + s[i].lower() + s[i + 1:])
                    next_s.append(s[0:i] + s[i].upper() + s[i + 1:])
            cur_s = next_s
        return cur_s

    def letterCasePermutation_1(self, S):
        """
        :type S: str
        :rtype: List[str]
        109ms
        """
        res = ['']
        for c in S:
            if c.isalpha():
                res = [j + i for i in [c.upper(), c.lower()] for j in res]
            else:
                res = [i + c for i in res]
        return res
print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("3z4"))
print(Solution().letterCasePermutation("12345"))

