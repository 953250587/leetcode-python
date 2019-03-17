"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    # 45ms
    def largestNumber(self, nums):
        l=len(str(max(nums)))
        a=str(l)
        c='{:?<'+a+'}'
        s=[c.format(str(i)) for i in nums]
        s1=sorted(s)
        ans=''
        # print(s1)
        for i in range(len(s1))[::-1]:
            if '?' in s1[i]:
                temp=s1[i].replace('?',s1[i][0])
                Return = False
                count=i
                for j in range(0,i)[::-1]:
                    if s1[j].replace('?',s1[j][0])<temp:
                        break
                    elif s1[j].replace('?',s1[j][0])==temp:
                        A=s1[count].replace('?','')+s1[j].replace('?','')
                        B=s1[j].replace('?','')+s1[count].replace('?','')
                        if A<B:
                            Return=True
                            s1[count],s1[j]=s1[j],s1[count]
                            count=j
                    else:
                        Return = True
                        s1[count], s1[j] = s1[j], s1[count]
                        count=j
                if Return:
                    i+=1
        for i in s1[::-1]:
            ans+=(i.replace('?',''))
        if int(ans)==0:
            return '0'
        # print(s1)
        return ans
    #py2
    #39ms
    def largestNumber_1(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(num).lstrip('0') or '0'

print(Solution().largestNumber([0,0]))
