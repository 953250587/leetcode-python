"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.



Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
         61 ms
        """
        if len(A) < 3:
            return 0
        before_val = A[0]
        start_num = 0
        end_num = 0
        ans = 0
        count = 1
        down = False
        up = False
        for a in A[1:]:
            if a == before_val:
                # 确保有上下两次
                if down and up:
                    ans = max(ans, end_num - start_num + 1)
                # 从当期位置开始记录
                start_num = count
                down = False
                up = False
            elif a < before_val:
                # 确保有上的过程
                if up:
                    end_num = count
                    down = True
                # 否则更新开始的位置
                else:
                    start_num = count
            else:
                # 如果有向下的过程，向下的过程只在有向上的过程之后才记录，所以肯定有
                # 值存在，记录最大情况，然后起始位置在这个之前一位
                if down:
                    ans = max(ans, end_num - start_num + 1)
                    start_num = count - 1
                    down = False
                # 不然就是认为是一个一般的向上的过程，记录最后的位置
                else:
                    end_num = count
                up = True
            count += 1
            before_val = a
            # print(a, ans)
        # 确保有上下两个过程
        if down and up:
            ans = max(ans, end_num - start_num + 1)
        return ans
# print(Solution().longestMountain([2,3]))
# print(Solution().longestMountain([2,1,4,7,3,2,5]))
# print(Solution().longestMountain([2,2,2]))
# print(Solution().longestMountain([4,3,2,1,0]))
# print(Solution().longestMountain([1,2,3,4,5,6]))
# print(Solution().longestMountain([1,1,2,3,2,1,9,8,7,5,3,9]))
# print(Solution().longestMountain([0,1,2,3,4,5,6,7,8,9]))
# print(Solution().longestMountain([9,8,7,6,5,4,3,2,1,0]))
# print(Solution().longestMountain([0,0,1,2,3,4,4,0,2,3]))
# print(Solution().longestMountain([0,1,0]))
# print(Solution().longestMountain([7,4,8]))
print(Solution().longestMountain([0,0,1,0,0,1,1,1,1,1]))



