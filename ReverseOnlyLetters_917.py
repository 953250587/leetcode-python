"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        20 ms
        """
        start = 0
        end = len(S) - 1
        chars = list(S)
        # 判断是否已经到达结束条件，如果start和end重合，说明已经无法移动了
        # 所以结束
        while start < end:
            # 不然判断是否最多到和end重合情况中的字母所在位置为止
            while start <= end and not chars[start].isalpha():
                start += 1
            # 同上
            while start <= end and not chars[end].isalpha():
                end -= 1
            # 交换两者位置
            if 0 <= start <= end < len(S):
                chars[start], chars[end] = chars[end], chars[start]
            # 更新下一次的移动起始位置
            start += 1
            end -= 1
        return ''.join(chars)


print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(Solution().reverseOnlyLetters("!!!!!"))
