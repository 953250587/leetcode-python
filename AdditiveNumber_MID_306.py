"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.

1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        42ms
        """
        def add(str1,str2):
            flag=False
            result=''
            l=max(len(str1),len(str2))
            for i in range(1,l+1):
                if i>len(str1):
                    a=0
                else:
                    a=int(str1[-i])
                if i>len(str2):
                    b=0
                else:
                    b=int(str2[-i])
                c=a+b
                if flag:
                    c += 1
                if c // 10 > 0:
                    flag = True
                else:
                    flag = False
                result += str(c % 10)
            if flag:
                result +=str(1)
            return result[::-1]
        l=len(num)
        for i in range(1,l-1):
            str1=num[:i]
            if len(str1)>1 and num[0]=='0':
                continue
            for j in range(i+1,l):
                str2=num[i:j]
                str3=num[j:]
                if len(str2)>1 and num[i]=='0':
                    continue
                elif len(str3)>1 and num[j]=='0':
                    continue
                else:
                    k=j
                    flag=True
                    str1_copy=str1[:]
                    str2_copy = str2[:]
                    while k<l:
                        result=add(str1_copy,str2_copy)
                        print(str1_copy, str2_copy,result)
                        l1=len(result)
                        if num[k:k+l1]!=result:
                            flag=False
                            break
                        else:
                            k+=l1
                        str1_copy=str2_copy
                        str2_copy=result
                    if flag:
                        return True
                # print(str1,str2,str3)
        return False

    def isAdditiveNumber_1(self, num):
        """
        :type num: str
        :rtype: bool
        32ms
        """
        for i in range(1, len(num) // 2 + 1):
            if num[0] == '0' and i > 1:
                break
            n1 = int(num[:i])
            for j in range(1, len(num[i:]) // 2 + 1):
                n2 = int(num[i:i + j])
                n3 = n1 + n2
                if num[i + j:].startswith(str(n3)):
                    if self.fab(n1, n2, num):
                        return True
        return False

    def fab(self, n1, n2, num):
        s = str(n1) + str(n2)
        while num.startswith(s):
            if num == s:
                return True
            n1, n2 = n2, n1 + n2
            s += str(n2)
        return False
print(Solution().isAdditiveNumber_1('01123'))