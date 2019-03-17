"""
A password is considered strong if below conditions are all met:

    It has at least 6 characters and at most 20 characters.
    It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
    It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        41ms
        """
        if s == '':
            return 6
        l = len(s)
        print('len', l)
        mark = [1] * 3
        def what(char):
            if char.isdigit():
                return 0
            elif char.isupper():
                return 1
            elif char.islower():
                return 2
            else:
                return 3
        for char in s:
            pos = what(char)
            if pos <= 2:
                mark[pos] = 0
        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p - 1] == s[p - 2]:
                length = 2
                while p < len(s) and s[p] == s[p - 1]:
                    length += 1
                    p += 1

                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                p += 1
        print(mark, one, two, change)
        if l < 6:
            return max(sum(mark), 6 - l)
        elif l <= 20:
            return max(sum(mark), change)
        else:
            s = l - 20
            change -= min(one, s) # len % 3 == 0最末尾每删除1个元素，相当于减少1次替换
            print(change)
            change -= min(two * 2, max(s - one, 0)) // 2 # len % 3 == 1最末尾每删除2个元素，相当于减少1次替换
            print(change)
            change -= max(s - one - 2 * two, 0) // 3 # len % 3 == 2最末尾每删除3个元素，相当于减少1次替换
            print(change)
            return  s + max(change, sum(mark))

    def strongPasswordChecker_1(self, s):
        """
        :type s: str
        :rtype: int
        33ms
        """
        missing_count = 3
        if any('a' <= letter <= 'z' for letter in s):
            missing_count -= 1
        if any('A' <= letter <= 'Z' for letter in s):
            missing_count -= 1
        if any(letter.isdigit() for letter in s):
            missing_count -= 1

        change_count = 0
        idx = 2
        one, two = 0, 0
        while idx < len(s):
            if s[idx] == s[idx - 1] == s[idx - 2]:
                length = 2
                while idx < len(s) and s[idx] == s[idx - 1]:
                    idx += 1
                    length += 1

                change_count += length // 3
                if length % 3 == 1:
                    two += 1
                elif length % 3 == 0:
                    one += 1
            else:
                idx += 1

        if len(s) < 6:
            return max(missing_count, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_count, change_count)
        else:
            remove = len(s) - 20

            change_count -= min(remove, one)
            change_count -= min(max(remove - one, 0), two * 2) / 2
            change_count -= max(remove - one - 2 * two, 0) / 3

            return remove + max(missing_count, change_count)
# print(Solution().strongPasswordChecker('11111'))
# print(Solution().strongPasswordChecker('A12333aavca'))
# print(Solution().strongPasswordChecker('111111111111000000000000'))
# print(Solution().strongPasswordChecker('123456abcABC'))
# print(Solution().strongPasswordChecker('12345678910111213141516'))
# print(Solution().strongPasswordChecker("aa123"))
# print(Solution().strongPasswordChecker("aaaabbaaabbaaa123456A"))
# print(Solution().strongPasswordChecker("1Abababcaaaabababababa"))
print(Solution().strongPasswordChecker("..................!!!"))

