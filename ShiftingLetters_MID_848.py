"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9

"""


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
         118 ms
        """
        result = []
        count = 0
        for i in shifts[::-1]:
            count += i
            count %= 26
            result.append(count)
        ans = []
        START = ord('a')
        for char in S:
            a = result.pop()
            x = ord(char) + a - START
            ans.append(chr(x % 26 + START))
        return ''.join(ans)

    def shiftingLetters_1(self, S, shifts):
        """
        116ms
        :param S:
        :param shifts:
        :return:
        """
        for i in range(len(shifts) - 1)[::-1]: shifts[i] += shifts[i + 1]
        return "".join(chr((ord(c) - 97 + s) % 26 + 97) for c, s in zip(S, shifts))

print(Solution().shiftingLetters(S = "abc", shifts = [3,5,9]))
print(Solution().shiftingLetters("ruu",[26,9,17]))