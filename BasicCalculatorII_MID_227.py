"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        249ms
        """
        nums=[]
        operation=[]
        num=''
        for i in s:
            if i.isdigit():
                num+=i
            elif i==' ':
                pass
            else:
                nums.append(int(num))
                num=''
                if len(operation)>=1 and  (operation[-1]=='*' or operation[-1]=='/'):
                    if operation[-1]=='*':
                        nums[-2]=nums[-1]*nums[-2]
                    else:
                        nums[-2] = nums[-2] // nums[-1]
                    nums=nums[:-1]
                    operation[-1]=i
                else:
                    operation.append(i)
        nums.append(int(num))
        count=0
        if len(operation)>=1 and operation[-1]=='*':
            nums[-2]=nums[-2]*nums[-1]
            operation = operation[:-1]
        elif len(operation)>=1 and operation[-1]=='/':
            nums[-2]=nums[-2]//nums[-1]
            operation = operation[:-1]

        # print(nums)
        for opera in operation:
            if opera=='+':
                nums[count+1]=nums[count]+nums[count+1]
            elif opera=='-':
                nums[count+1]=nums[count]-nums[count+1]
            elif opera=='*':
                nums[count+1]=nums[count]*nums[count+1]
            else:
                nums[count+1] = nums[count] // nums[count+1]
            count+=1
        # print(nums)
        return nums[count]

    def calculate_1(self, s):
        """
        :type s: str
        :rtype: int
        115ms
        """

        s = s + "+"  # guard
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            print(stack)
            if ss.isdigit():  # deal with numbers
                num = 10 * num + ord(ss) - ord("0")  # faster than int(ss)
            elif ss in "+-":
                if stack and stack[-1] in "*/":  # update number in a "*/" expression
                    md, val = stack.pop(), stack.pop()
                    num = val * num if md == "*" else val / num
                res, num, sign = res + sign * num, 0, [-1, 1][ss == "+"]
            elif ss in "*/":
                if stack and stack[-1] in "*/":  # update number in a "*/" expression
                    md, val = stack.pop(), stack.pop()
                    num = val * num if md == "*" else val / num
                stack.extend([num, ss])  # if no previous "*/", append directly
                num = 0
        return res

print(Solution().calculate_1("1+3*10/10" ))
# a=[]
# for i in range(10):
#     a.append(str(i))
# print(a)
# a.remove(str(8))
# print(a)