"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        135ms
        """
        max_num=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                max_num+=1
                if i-1>=0:
                    #max_num+=1
                    flowerbed[i-1]=2
                if i+1<len(flowerbed):
                    if (i+2<len(flowerbed) and flowerbed[i+2]!=1) or i+2>=len(flowerbed):
                        #max_num+=1
                        flowerbed[i + 1] = 2
        print(flowerbed)
        sum=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i+1<len(flowerbed):
                    flowerbed[i+1]=2
                sum+=1
        return sum>=n
    # 112ms
    def canPlaceFlowers_1(self, A, N):
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i - 1] == 0)
                and (i == len(A) - 1 or A[i + 1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0
print(Solution().canPlaceFlowers([0,1,0],1))
print(Solution().canPlaceFlowers([1,0,1,0,1,0],2))
print(Solution().canPlaceFlowers([1,0,0,0,1,0,1],1))
print(Solution().canPlaceFlowers([1,0,0,0,1,0,0],2))
