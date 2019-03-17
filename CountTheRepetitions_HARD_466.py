"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2

"""


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0
        cur = n1
        dicts = {0: 0}
        n, m = 0, 0
        s2 = s2 * n2
        ls1 = len(s1)
        ls2 = len(s2)
        i, j = 0, 0
        print(ls1, ls2)
        flag_j = False
        while i < n1 * ls1:
            flag_i = False
            # print('i', i, 'm', m)
            if s1[i % ls1] == s2[j % ls2]:
                if j % ls2 == ls2 - 1:
                    m += 1
                    flag_j = True
                else:
                    flag_j = False
                j += 1
            if i % ls1 == ls1 - 1:
                n += 1
                dicts[n] = m
                flag_i = True
            if flag_i and flag_j:
                cur = n
                break
            i += 1
        print('cur', cur)
        print(dicts)
        return (n1 // cur) * dicts[cur] + dicts[n1 % cur]

    def getMaxRepetitions_1(self, s1, n1, s2, n2):
        """
        44ms
        :param s1:
        :param n1:
        :param s2:
        :param n2:
        :return:
        """

        if any(c for c in set(s2) if c not in set(s1)):  # early return if impossible
            return 0

        s2_index_to_reps = {0: (0, 0)}  # mapping from index in s2 to numbers of repetitions of s1 and s2
        i, j = 0, 0
        s1_reps, s2_reps = 0, 0

        while s1_reps < n1:

            if s1[i] == s2[j]:
                j += 1  # move s2 pointer if chars match
            i += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

            if i == len(s1):
                i = 0
                s1_reps += 1
                if j in s2_index_to_reps:  # loop found, same index in s2 as seen before
                    break
                s2_index_to_reps[j] = (s1_reps, s2_reps)

        if s1_reps == n1:  # already used n1 copies of s1
            return s2_reps // n2

        initial_s1_reps, initial_s2_reps = s2_index_to_reps[j]  # repetitions before loop starts
        loop_s1_reps = s1_reps - initial_s1_reps
        loop_s2_reps = s2_reps - initial_s2_reps
        loops = (n1 - initial_s1_reps) // loop_s1_reps

        s2_reps = initial_s2_reps + loops * loop_s2_reps
        s1_reps = initial_s1_reps + loops * loop_s1_reps

        while s1_reps < n1:  # if loop does not end with n1 copies of s1, keep going

            if s1[i] == s2[j]:
                j += 1
            i += 1

            if i == len(s1):
                i = 0
                s1_reps += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

        return s2_reps // n2
# print(Solution().getMaxRepetitions('acb', 4, 'ab', 2))
# print(Solution().getMaxRepetitions('aaaa', 3, 'a', 10))
# print(Solution().getMaxRepetitions('baba',  11, 'baab', 1))
# print(Solution().getMaxRepetitions('aaa', 3, 'aa', 1))
print(Solution().getMaxRepetitions("lovelivenanjomusicforever",10000,"nanjo",10))
