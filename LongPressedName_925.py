"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        32 ms
        """
        if len(typed) == 0:
            return len(name) == len(typed) == 0

        # 用于把字符串转化为连续字母个数的形式，比如 aaleex->[['a', 2], ['l', 1], ['e', 2], ['x', 1]]
        def change(typed):
            start = typed[0]
            t = []
            count = 1
            for char in typed[1:]:
                if char == start:
                    count += 1
                else:
                    t.append([start, count])
                    count = 1
                start = char
            t.append([start, count])
            return t

        t1 = change(name)
        t2 = change(typed)
        # 长度不一致肯定不行
        if len(t1) != len(t2):
            return False
        else:
            for i in range(len(t1)):
                # 字母不一致或者个数不够也不行
                if t1[i][0] != t2[i][0] or t1[i][1] > t2[i][1]:
                    return False
            return True

    def isLongPressedName_1(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        36ms
        """
        if len(name) == 0:
            return True

        if len(name) > len(typed):
            return False

        i, j = 0, 0
        while i < len(name):
            if name[i] != typed[j]:
                j += 1
            else:
                i += 1
                j += 1
            if j == len(typed):
                break

        return i == len(name)


print(Solution().isLongPressedName(name = "alex", typed = "aaleex"))
print(Solution().isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(Solution().isLongPressedName(name = "leelee", typed = "lleeelee"))
print(Solution().isLongPressedName(name = "laiden", typed = "laiden"))


