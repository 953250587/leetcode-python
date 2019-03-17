"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        225ms
        """
        result=[0]
        if num<=0:
            return result
        count=1
        start=1
        result.append(1)
        while start+count<=num:
            for i in result[start:start+count]:
                result.append(i)
                result.append(i+1)
            start+=count
            print(start,count)
            count*=2
        return result[:num+1]

    def countBits_1(self, num):
        """
        :type num: int
        :rtype: List[int]
        175ms
        """
        if num == 0:
            return [0]
        result = [0, 1]
        length = 1
        while (len(result) < num + 1):
            to_add = result[-length:]
            result += to_add + [x + 1 for x in to_add]
            length *= 2
        return result[0:(num + 1)]
print(Solution().countBits(13))

