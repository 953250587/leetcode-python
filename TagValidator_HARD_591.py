"""
Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

    The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
    A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
    A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
    A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
    A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
    A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
    The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
    CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.

Valid Code Examples:

Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output: True

Explanation:

The code is wrapped in a closed tag : <DIV> and </DIV>.

The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.

Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

So TAG_CONTENT is valid, and then the code is valid. Thus return true.


Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output: True

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content could also be separated into : text1|cdata|text2.

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

text2 -> "]]>>]"


The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.

Invalid Code Examples:

Input: "<A>  <B> </A>   </B>"
Output: False
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Input: "<DIV>  div tag is not closed  <DIV>"
Output: False

Input: "<DIV>  unmatched <  </DIV>"
Output: False

Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
Output: False

Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
Output: False

Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
Output: False

Note:

    For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.

"""
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        40ms
        """
        if len(code) < 7: #<A></A>最少个数
            return False
        if code[0] != '<' or code[-1] != '>' or code[:2] == '<!' or  code[:2] == '</':
            return False
        i = 1
        l = len(code)
        stack = []
        while i < l:
            print('cur', i, code[i])
            if code[i] == '!':
                i += 1
                if code[i: i + 7] == '[CDATA[':
                    i += 7
                    flag = False
                    while i < l:
                        if code[i: i + 3] == ']]>':
                            flag = True
                            break
                        i += 1
                    if not flag:
                        print('1')
                        return False
                else:
                    print('2')
                    return False
            elif code[i] == '/':
                tag = ''
                i += 1
                while i < l and code[i] != '>':
                    if code[i].isupper():
                        tag += code[i]
                    else:
                        return False
                    i += 1
                if tag == stack[-1]:
                    stack.pop()
                    if i + 1 < l and stack == []:
                        print('3')
                        return False
                else:
                    return False
            else:
                tag = ''
                while i < l and code[i] != '>':
                    if code[i].isupper():
                        tag += code[i]
                    else:
                        print('4')
                        return False
                    i += 1
                if len(tag) > 9 or len(tag) < 1:
                    print('5')
                    return False
                stack.append(tag)
            while i < l and code[i] != '<':
                i += 1
            i += 1
            print(stack)
        print('finally', stack)
        if stack == []:
            return True
        else:
            return False

    def isValid_1(self, code):
            """
            :type code: str
            :rtype: bool
            42ms
            """

            my_stack = []
            idx, size = 0, len(code)
            while idx < size:
                if code[idx] == '<':
                    if idx + 8 < size and code[idx + 1:idx + 9] == "![CDATA[":
                        if not my_stack:
                            return False

                        while idx + 3 < size and code[idx:idx + 3] != "]]>":
                            idx += 1

                        if idx + 3 >= size:
                            return False

                        idx += 3
                    else:
                        left = idx
                        while idx < size and code[idx] != '>':
                            idx += 1

                        if idx == size:
                            return False

                        tag_name = code[left + 1:idx]
                        if not tag_name:
                            return False

                        if tag_name[0] == '/':
                            if not my_stack or my_stack[-1] != tag_name[1:]:
                                return False

                            my_stack.pop()
                            if not my_stack:
                                return idx == size - 1
                        else:
                            if len(tag_name) < 1 or len(tag_name) > 9:
                                return False

                            for char in tag_name:
                                if char < 'A' or char > 'Z':
                                    return False

                            my_stack.append(tag_name)

                        idx += 1
                else:
                    if not my_stack:
                        return False

                    idx += 1
            return False


# print(Solution().isValid('1'))
# print(Solution().isValid('<DIV>This is the first line <![CDATA[<div>]]></DIV>'))
# print(Solution().isValid('<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>'))
# print(Solution().isValid('<A>  <B> </A>   </B>'))
# print(Solution().isValid('<DIV>  div tag is not closed  <DIV>'))
# print(Solution().isValid('<DIV>  unmatched <  </DIV>'))
# print(Solution().isValid('<DIV> closed tags with invalid tag name  <b>123</b> </DIV>'))
# print(Solution().isValid('<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>'))
# print(Solution().isValid('<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>'))

# print(Solution().isValid('<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>'))
# print(Solution().isValid("<A><A>/A></A></A>"))  # True
# print(Solution().isValid('<A></A><B></B>')) # False
# print(Solution().isValid("<A><B></B></A>" ))  # True
# print(Solution().isValid("<A>![CDATA[/A>]]></A>" )) # True
# print(Solution().isValid("123456" )) # False
# print(Solution().isValid("<A></A>")) # True
# print(Solution().isValid("<A></A>>")) # False
# print(Solution().isValid("<DIV>>>>>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")) # True
# print(Solution().isValid("<AAAAAAAAAA></AAAAAAAAAA>")) # False
# print(Solution().isValid("<a><a></a></a>")) # False
# print(Solution().isValid("<A><!CDATAA[[123]]></A>")) # False
# print(Solution().isValid("!!!<A>123</A>123")) # False
# print(Solution().isValid("<A>123</A>123" )) # False

print(Solution().isValid("<A><![CDATA[<B></A>]]></B></A>"))