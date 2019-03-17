"""
 Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a=[str(i+1) for i in range(n)]
        b=sorted(a)
        b=[int(i) for i in b]
        return b

    def lexicalOrder_1(self, n):
        """
        :type n: int
        :rtype: List[int]
        1509ms
        """
        self.n=n
        self.list=[]
        self.flag=True

        def tenble(num,count):
            if count==1:
                for i in range(1, 10):
                    if 10 * num + i > self.n:
                        self.flag=False
                        return
                    self.list.append(10 * num + i)
                    if self.flag:
                        tenble(10 * num + i,count+1)
            else:
                for i in range(0, 10):
                    if 10 * num + i > self.n:
                        self.flag = False
                        return
                    self.list.append(10 * num + i)
                    if self.flag:
                        tenble(10 * num + i,count+1)
            self.flag=True

        tenble(0,1)
        return self.list

    def lexicalOrder_3(self, n):
        """
        :type n: int
        :rtype: List[int]
        755ms
        """
        if n < 1:
            return []
        result = []
        self.generate(1, result, n)
        return result

    def generate(self, start, result, n):
        for i in range(start, (start // 10) * 10 + 10):
            if i <= n:
                result.append(i)
                if i * 10 <= n:
                    self.generate(i * 10, result, n)
            else:
                break
        return



print(Solution().lexicalOrder_1(49999))
print(Solution().lexicalOrder(49999))