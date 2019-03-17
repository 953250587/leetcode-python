"""
 Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

    The given number is in the range [0, 108]

"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        49ms
        """
        s = list(str(num))
        d = sorted(s, reverse = True)
        l = len(s)
        is_Swap = False
        for i in range(l):
            if d[i] != s[i]:
                is_Swap = True
                end = i
                target = d[i]
                break
        if not is_Swap:
            return num
        for i in range(l - 1, end, -1):
            if s[i] == target:
                s[end], s[i] = s[i], s[end]
                break
        return int(''.join(s))

    def maximumSwap_1(self, num):
        """
        :type num: int
        :rtype: int
        29ms
        """
        if num < 10:
            return num
        max_num = str(num)
        s = [c for c in str(num)]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                s[i], s[j] = s[j], s[i]
                now = ''.join(s)
                if int(max_num) < int(now):
                    max_num = ''.join(s)
                s[i], s[j] = s[j], s[i]
        return int(max_num)

    def maximumSwap_2(self, num):
        """
        :type num: int
        :rtype: int
        38ms
        """
        s_copy = list(str(num))
        sorted_s_copy = sorted(s_copy, reverse=True)

        n = len(s_copy)
        swap_i = None
        swap_numb = None
        for i in range(n):
            if not s_copy[i] == sorted_s_copy[i]:
                swap_i = i
                swap_numb = sorted_s_copy[i]
                break

        # find rightmost swap_numb
        if not swap_i == None:
            for i in range(n):
                if s_copy[n - 1 - i] == swap_numb:
                    temp = s_copy[swap_i]
                    s_copy[swap_i] = s_copy[n - 1 - i]
                    s_copy[n - 1 - i] = temp
                    return int(''.join(s_copy))
        return num
print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(882736))
print(Solution().maximumSwap(27376))
print(Solution().maximumSwap(101))

