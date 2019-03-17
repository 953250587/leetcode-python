"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:

    Elements of the given array are in the range of 0 to 10^9
    Length of the array will not exceed 10^4.

"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        969ms
        """
        l=len(nums)
        result=0
        for i in range(32):
            count=0
            for j in nums:
                b=j>>i
                if bin(b)[-1]=='1':
                    count+=1
            result+=(l-count)*count
        return result

     # 302ms   return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

    def totalHammingDistance_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        212ms
        """
        n = len(nums)

        ans = 0
        for i in range(16):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 0x10001

            cnt0, cnt1 = cnt & 0xFFFF, cnt >> 16
            ans += cnt0 * (n - cnt0) + cnt1 * (n - cnt1)

        return ans
print(Solution().totalHammingDistance([]))
print(4,3,20^19,20|19,4&3)