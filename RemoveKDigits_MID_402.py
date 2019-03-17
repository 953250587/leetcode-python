"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        38ms
        """
        if len(num)==k:
            return '0'
        if k==0:
            return num
        stack=[]
        temp=num[0]
        stack.append(temp)
        flag=False
        count=0
        result=''
        for i in num[1:]:
            count+=1
            if i>=temp:
                stack.append(i)
            else:
                while len(stack)>0:
                    if stack[-1]>i:
                        stack.pop()
                        k-=1
                        if k==0:
                            flag=True
                            break
                    else:
                        break
                if flag:
                    result=''.join(stack)+num[count:]
                    break
                else:
                    stack.append(i)
            temp=i
        if not flag:
            result=''.join(stack[:-k])
        a=result.lstrip('0')
        if  a== '':
            return '0'
        else:
            return a

    def removeKdigits_1(self, num, k):
            """
            :type num: str
            :type k: int
            :rtype: str
            45ms
            """
            st = []
            for d in num:
                while k and st and st[-1] > d:
                    st.pop()
                    k -= 1
                st.append(d)
            return ''.join(st[:-k or None]).lstrip('0') or '0'
num = "1432219"
k = 3
print(Solution().removeKdigits(num,k))
num = "10200"
k = 1
print(Solution().removeKdigits(num,k))
num = "10"
k = 2
print(Solution().removeKdigits(num,k))
num = "12134565"
k = 2
print(Solution().removeKdigits(num,k))
num = ""
k = 0
print(Solution().removeKdigits(num,k))
num = "10"
k = 1
print(Solution().removeKdigits(num,k))
num = "12345"
k = 0
print(Solution().removeKdigits(num,k))