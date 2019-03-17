"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.



Note:

    S has length at most 26, and no character is repeated in S.
    T has length at most 200.
    S and T consist of lowercase letters only.


"""
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        39MS
        """
        import heapq, collections
        h = []
        char_dicts = collections.defaultdict(int)
        # 把S中每个字符按出现顺序记录，没出现的字符默认为0
        for i, char in enumerate(S):
            char_dicts[char] = i + 1
        # 把T中字符按S的顺序编号放入heapy中
        for char in T:
            heapq.heappush(h, (char_dicts[char], char))
        ans = ''
        # 标号从小到大取出，重构T
        while h:
            ans += heapq.heappop(h)[1]
        return ans

    def customSortString_1(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        33MS
        """
        R = ""
        # 找出每次最优的字母
        for char in S:
            while char in T:
                # 如果T中有这个字符，取出来放前面
                T = T.replace(char, "", 1)
                R += char
        # 优先的放前面，剩余的放后面
        return R + T


    def customSortString_2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        40MS
        """
        R = ""
        # 找出每次最优的字母
        T = list(T)
        for char in S:
            for i, T_char in enumerate(T):
                if T_char == char:
                    R += char
                    T[i] = ''
            # while char in T:
            #     # 如果T中有这个字符，取出来放前面
            #     T = T.replace(char, "", 1)
            #     R += char
        # 优先的放前面，剩余的放后面
        return R + ''.join(T)
print(Solution().customSortString_2(S = "cba", T = "abcd"))

