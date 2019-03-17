"""
 Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:

    The length of given words won't exceed 500.
    Characters in given words can only be lower-case letters.

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        812ms
        """
        l = min(len(word1), len(word2))
        mark = [510] * (l + 1)
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        for num_i, i in enumerate(word2):
            mark_copy = mark.copy()
            for num, j in enumerate(word1):
                if i == j:
                    print(num_i, j ,num)
                    sets = set()
                    for k in range(1, num_i + 2):
                        sets.add(mark[k])
                        if mark[k] > num and num not in sets:
                            mark_copy[k] = min(num, mark_copy[k])
                            break
                    print(mark_copy)
            mark = mark_copy

        for num in range(l, 0, -1):
            if mark[num] != 510:
                return len(word1) + len(word2) - 2 * num
        return len(word1) + len(word2)

    def minDistance_1(self, word1, word2):
        """
                :type word1: str
                :type word2: str
                :rtype: int
                469ms
                """
        l1, l2 = len(word1), len(word2)
        if l1 * l2 == 0:
            return l1 + l2

        l1, l2 = len(word1), len(word2)
        T = [None] * l1
        for i in range(l1):
            T[i] = [-1] * l2

        # initialize T[:][0]
        if word1[0] not in word2:
            for j in range(l2):
                T[0][j] = 0
        else:
            first = word2.index(word1[0])
            for j in range(l2):
                if j < first:
                    T[0][j] = 0
                else:
                    T[0][j] = 1
        # initialize T[0][:]
        if word2[0] not in word1:
            for i in range(l1):
                T[i][0] = 0
        else:
            first = word1.index(word2[0])
            for i in range(l1):
                if i < first:
                    T[i][0] = 0
                else:
                    T[i][0] = 1
        # update T for general T[i][j]
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i] == word2[j]:
                    T[i][j] = T[i - 1][j - 1] + 1
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])
        return l1 + l2 - 2 * T[l1 - 1][l2 - 1]

    def minDistance_2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        379ms
        """
        len1, len2 = len(word1), len(word2)
        dp = [0] * (len2 + 1)
        for char1 in word1:
            tmp = [0] * (len2 + 1)
            for i, char2 in enumerate(word2):
                tmp[i + 1] = max(dp[i + 1], tmp[i], dp[i] + (char1 == char2))
            dp = tmp
        return len1 + len2 - 2 * dp[-1]
    
word1 = "sea"
word2 = "eat"
print(Solution().minDistance(word1, word2))
# # #
word1 = "abct"
word2 = "atbc"
print(Solution().minDistance(word1, word2))
# #
word1 = "food"
word2 = "money"
print(Solution().minDistance(word1, word2))
# #
word1 = "kitten"
word2 = "sitting"
print(Solution().minDistance(word1, word2))

# word1 = "di ni t rop h en ylhy drazine"
# word2 = "di me th ylhydrazine"
# # print(Solution().minDistance(word1, word2))
#
word1 = "dinitrophenylhydrazine"
word2 = "dimethylhydrazine"
print(Solution().minDistance(word1, word2))

word1 = "zoo logicoar ch ae ologist"
word2 = "zoo psy ch ologist"

word1 = "zoologicoarchaeologist"
word2 = "zoopsychologist"
print(Solution().minDistance(word1, word2))