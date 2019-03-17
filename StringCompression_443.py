"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        79ms
        """
        temp = chars[0]
        count = 1
        start = 0
        for char in chars[1:]:
            if char == temp:
                count += 1
            else:
                if count == 1:
                    chars[start] = temp
                    start += 1
                else:
                    chars[start] = temp
                    start += 1
                    s = str(count)
                    for c in s:
                        chars[start] = c
                        start += 1
                temp = char
                count = 1
        if count == 1:
            chars[start] = temp
            start += 1
        else:
            chars[start] = temp
            start += 1
            s = str(count)
            for c in s:
                chars[start] = c
                start += 1
        return start

    def compress_1(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        79ms
        """
        length = len(chars)

        letter_index = 0
        digit_index = 1
        curr_char = chars[0]
        count = 1

        for i in range(1, length):
            if chars[i] == curr_char:
                count = count + 1
                chars[i] = ""
            else:
                chars[letter_index] = curr_char
                if count != 1:
                    for digit in str(count):
                        if (digit_index < i):
                            chars[digit_index] = digit
                            digit_index = digit_index + 1

                letter_index = digit_index
                digit_index = letter_index + 1
                curr_char = chars[i]
                chars[i] = ""
                count = 1

        chars[letter_index] = curr_char
        if count != 1:
            for digit in str(count):
                if (digit_index < length):
                    chars[digit_index] = digit
                    digit_index = digit_index + 1

        # print chars

        while True:
            if chars[-1] != "":
                break
            del chars[-1]
chars = ["a","a","b","b","c","c","c"]
a = Solution().compress(chars)
print(chars[:a], a)

chars = ["a"]
a = Solution().compress(chars)
print(chars[:a], a)


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
a = Solution().compress(chars)
print(chars[:a], a)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b",'c']
a = Solution().compress(chars)
print(chars[:a], a)

