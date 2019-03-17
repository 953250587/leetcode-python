"""
 Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        28ms
        """
        self.s=s
        stack=[]
        self.s=s.split('[')
        print(self.s)
        if len(self.s)==1:
            return s
        for i in self.s:
            if i.isdigit():
                stack.append(i)
            else:
                if ']' not in i:
                    stack.append(i)
                else:
                    p=i.split(']')
                    b=''
                    for p1 in p[:-1]:
                        b=b+p1
                        a=stack.pop()
                        k = 0
                        while k < len(a) and not a[k].isdigit():
                            k += 1
                        abc = a[:k]
                        num = a[k:]
                        if len(num) > 0:
                            b=abc + int(num) * b
                        else:
                            b=abc+b
                    stack.append(b+p[-1])
                    print(stack)
        return stack[0]

    def decodeString_1(self, s):
        # iterative, 掏心法。
        result_stack = []
        result_stack.append(["", 1])  # "" is result, times 1.
        num_repeats = ""
        for index in range(len(s)):
            if s[index].isdigit():
                num_repeats += s[index]
            if s[index] == "[":
                result_stack.append(["", int(num_repeats)])
                num_repeats = ""
            if s[index] == "]":
                current_word, number = result_stack.pop()
                result_stack[-1][0] += number * current_word
            if s[index].isalpha():
                result_stack[-1][0] += s[index]
        return result_stack[0][0]
print(Solution().decodeString("sd2[f2[e]g]i"))
print(Solution().decodeString("2[2[b]]"))
print(Solution().decodeString("2[2[2[b]]]"))
print(Solution().decodeString("2[abc]xyz3[z]"))
print(Solution().decodeString('2[abc]3[cd]ef'))
print(Solution().decodeString('3[a2[c]ef]i'))
print(Solution().decodeString('abc2[abc]3[d4[a]ef]'))
