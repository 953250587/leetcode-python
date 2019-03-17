"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function.
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        459ms
        """
        stack = []
        num = ''
        s = s.strip()
        s += '+'
        for char in s:
            if char == ' ':
                continue
            if char.isdigit():
                num += char
            if char in '+-':
                if not stack or stack[-1] == '(':
                    stack.append(num)
                else:
                    mark = stack.pop()
                    before_num = stack.pop()
                    if mark == '+':
                        ans = int(before_num) + int(num)
                    else:
                        ans = int(before_num) - int(num)
                    stack.append(str(ans))
                stack.append(char)
                num = ''
            if char == '(':
                stack.append(char)
            if char == ')':
                if stack[-1] != '(':
                    mark = stack.pop()
                    before_num = stack.pop()
                    if mark == '+':
                        ans = int(before_num) + int(num)
                    else:
                        ans = int(before_num) - int(num)
                    num = str(ans)
                else:
                    ans = int(num)
                stack.pop()
                if stack:
                    mark = stack.pop()
                    before_num = stack.pop()
                    if mark == '+':
                        ans = int(before_num) + int(num)
                    else:
                        ans = int(before_num) - int(num)
                num = str(ans)
        return int(stack[0])


    def calculate_1(self, s):
        """
        229ms
        :param s:
        :return:
        """

        total=0
        sign=1
        stk=[]
        n=0

        i=0
        while i<len(s):
            if s[i].isdigit():
               n=n*10+int(s[i])
            elif s[i]=='+':
                total+=(n*sign)
                n=0
                sign=1
            elif s[i]=='-':
                total+=(n*sign)
                n=0
                sign=-1
            elif s[i]=='(':
                stk.append(total)
                stk.append(sign)
                total=0
                sign=1
            elif s[i]==')':
                total+=(n*sign)
                presign=stk.pop()
                pretotal=stk.pop()
                total = pretotal + presign*total
                n=0
                sign=1

            #print s[i:]
            #print total, n, sign, stk

            i+=1

        total = total + sign*n

        return total

    def calculate_2(self, s):
        """
        :type s: str
        :rtype: int
        99ms
        """
        stack = [0]
        signs = [1]
        d = 0
        sign = 1

        for n in '({})'.format(s):
            if n.isdigit():
                d = d * 10 + ord(n) - ord('0')
            elif n == '+':
                stack[-1] += sign * d
                sign, d = 1, 0
            elif n == '-':
                stack[-1] += sign * d
                sign, d = -1, 0
            elif n == '(':
                stack.append(0)
                signs.append(sign)
                sign = 1
            elif n == ')':
                stack[-1] += sign * d
                d, sign = stack.pop(), signs.pop()
                stack[-1] += d * sign
                sign, d = 1, 0

        return stack[-1]
print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 2-1 + 2 "))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("(1)"))
print(Solution().calculate('0'))

