"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Example 1:
Input:
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

Explanation:
The string
/*
 denotes a block comment, including line 1 and lines 6-9. The string
//
 denotes line 4 as comments.
Example 2:
Input:
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
Note:

The length of source is in the range [1, 100].
The length of source[i] is in the range [0, 80].
Every open block comment is eventually closed.
There are no single-quote, double-quote, or control characters in the source code.
"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        32ms
        """
        result = []
        block = False
        union = False
        start = 0
        while start < len(source):
            line = source[start]
            start += 1
            if not block and '//' in line and '/*' in line:
                s = line.split('//', 1)
                if '/*' not in s[0]:
                    s = line.split('//', 1)
                    if len(s[0]) >= 1:
                        if union:
                            result[-1] += s[0]
                            union = False
                        else:
                            result.append(s[0])
                    union = False
                else:
                    block = True
                    s = line.split('/*', 1)
                    if len(s[0]) >= 1:
                        if union:
                            result[-1] += s[0]
                        else:
                            union = True
                            result.append(s[0])
                    source.insert(start, s[1])
            elif not block and '//' in line:
                s = line.split('//', 1)
                if len(s[0]) >= 1:
                    if union:
                        result[-1] += s[0]
                    else:
                        result.append(s[0])
                union = False
            elif not block and '/*' in line:
                block = True
                s = line.split('/*', 1)
                if len(s[0]) >= 1:
                    if union:
                        result[-1] += s[0]
                    else:
                        union = True
                        result.append(s[0])
                source.insert(start, s[1])
            elif block and '*/' in line:
                end = line.split('*/', 1)[1]
                source.insert(start, end)
                block = False
            elif not block:
                if union:
                    result[-1] += line
                    union = False
                else:
                    if len(line) >= 1:
                        result.append(line)
            print(source, union, block)
            print(result)
        return result


# source = ["/*Test program */",
#           "int main()",
#           "{ ",
#           "  // variable declaration ",
#           "int a, b, c;",
#           "",
#           "/* This is a test",
#           "   multiline  ",
#           "   comment for ",
#           "   testing */",
#           "a = b + c;",
#           "}"]
# a = Solution().removeComments(source)
# for i in a:
#     print(i)
#
# source =  ["a/*comment", "line", "more_comment*/b"]
# a = Solution().removeComments(source)
# for i in a:
#     print(i)
#
# source = ["a//*b//*c","blank","d/*/e*//f"]
# a = Solution().removeComments(source)
# for i in a:
#     print(i)
#
# source = ["a/*/b//*c","blank","d/*/e*//f"]
# a = Solution().removeComments(source)
# for i in a:
#     print(i)
#
# source = ["class test{",
#           "public: ",
#           "   int x = 1;",
#           "   /*double y = 1;*/",
#           "   char c;", "};"]
# a = Solution().removeComments(source)
# for i in a:
#     print(i)

source = ['d/*/aee*//d/********/']
a = Solution().removeComments(source)
for i in a:
    print(i)


def _find_comment(line):
    for i, ch in enumerate(line):
        if ch == '/' and i + 1 < len(line):
            ch = line[i + 1]
            if ch == '/' or ch == '*':
                return i
    return -1


# O(n) time. O(1) space.
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        36ms
        """
        row = 0
        while row < len(source):
            line = source[row]
            lo = _find_comment(line)

            if lo == -1:
                row += 1
                continue

            if line[lo + 1] == '/':
                if lo == 0:
                    source.pop(row)
                else:
                    source[row] = line[:lo]
                    row += 1
                continue

            hi = line.find('*/', lo + 2)
            if hi != -1:
                if lo == 0 and hi + 2 == len(line):
                    source.pop(row)
                else:
                    source[row] = line[:lo] + line[hi + 2:]
                continue

            if lo == 0:
                source.pop(row)
            else:
                source[row] = line[:lo]
                row += 1

            while row < len(source):
                line = source[row]
                hi = line.find('*/')
                if hi == -1:
                    source.pop(row)
                    continue

                if hi + 2 == len(line):
                    source.pop(row)
                else:
                    if lo == 0:
                        source[row] = line[hi + 2:]
                    else:
                        source.pop(row)
                        row -= 1
                        source[row] += line[hi + 2:]
                break

        return source