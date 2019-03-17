"""
 Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        73ms
        """
        import collections
        dicts = collections.Counter(s)
        mark = [0] * 26
        print(dicts)
        result = []
        for char in s:
            while result and ord(result[-1]) > ord(char) and dicts[result[-1]] > 0 and mark[ord(char) - ord('a')] == 0:
                a = result.pop()
                mark[ord(a) - ord('a')] = 0
            dicts[char] -= 1
            if mark[ord(char) - ord('a')] == 0:
                result.append(char)
                mark[ord(char) - ord('a')] = 1
        return ''.join(result)

    def removeDuplicateLettersOld(self, s):
        """
        :type s: str
        :rtype: str
        49ms
        """
        outPutStack = []  # the resultant letters
        letterCount = [0] * 26  # count of each letter in the string
        for c in s:
            letterCount[ord(c) - ord('a')] += 1
        placed = [False] * 26  # if the char is placed in out put

        for c in s:
            index = ord(c) - ord('a')
            if placed[index]:
                # dup, previously placed
                letterCount[index] -= 1
                continue
            # check the prev char, if qualified to be re-placed
            while len(outPutStack) > 0:
                pre_char = outPutStack[-1]
                pre_char_index = ord(pre_char) - ord('a')
                if letterCount[pre_char_index] > 0 and pre_char > c:  # more to come and bigger
                    outPutStack.pop()
                    placed[pre_char_index] = False
                else:
                    break

            outPutStack.append(c)
            placed[index] = True
            letterCount[index] -= 1
        return ''.join(outPutStack)

    def removeDuplicateLetters_1(self, s):
        """
        :type s: str
        :rtype: str
        46ms
        """
        counts = {}
        for c in s:
            counts[c] = 1 if c not in counts else counts[c] + 1
        visited = {c: False for c in counts}

        stack = []
        for c in s:
            counts[c] -= 1
            if not visited[c]:

                while stack and counts[stack[-1]] > 0 and stack[-1] > c:
                    visited[stack[-1]] = False
                    stack.pop()

                stack.append(c)
                visited[c] = True

        return ''.join(stack)
print(Solution().removeDuplicateLetters("bcabc"))
print(Solution().removeDuplicateLetters("cbacdcbc"))
print(Solution().removeDuplicateLetters("abacb"))