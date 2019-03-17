"""
 Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

Example 2:

Input: 21
Output: -1

"""
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        32ms
        """
        def next_greater(num):
            s = list(str(num))
            l = len(s)
            for i in range(l - 2, -1, -1):
                for j in range(l - 1, i, -1):
                    if int(s[j]) > int(s[i]):
                        s[i], s[j] = s[j], s[i]
                        s_2 = sorted(s[i + 1:])
                        s = s[0: i+1] + s_2
                        return s
            return -1
        a = 2147483647
        if n // 10 == 0:
            return -1
        b = next_greater(n)
        if b == -1:
            return -1
        else:
            s_1 = 0
            print(b)
            for i in b:
                s_1 = s_1 * 10 +int(i)
                print(s_1)
            if s_1 > a:
                return -1
            else:
                return s_1

    def nextGreaterElement_1(self, n):
        """
        :type n: int
        :rtype: int
        29ms
        """
        index1 = -1
        n = list(str(n))
        for i in range(len(n) - 1, 0, -1):
            if n[i - 1] < n[i]:
                index1 = i - 1
                break

        if index1 == -1:
            return -1


        index2 = index1 + 1
        temp = n[index1]
        larger = n[index1 + 1]
        for i in range(index1 + 1, len(n)):
            if n[i] > temp and n[i] < larger:
                larger = n[i]
                index2 = i
    
        # swap the two digits
        n[index1], n[index2] = n[index2], n[index1]
        n[index1 + 1:] = sorted(n[index1 + 1:])
        if int("".join(n)) < 2 ** 31 - 1:
            return int("".join(n))
        else:
            return -1
print(Solution().nextGreaterElement(12))
print(Solution().nextGreaterElement(12222333))
print(Solution().nextGreaterElement(12443322))