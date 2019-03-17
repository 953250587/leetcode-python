"""
We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
Input: nums = [1, 1, 2]
Output: false
Explanation:
Alice has two choices: erase 1 or erase 2.
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose.
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:

    1 <= N <= 1000.
    0 <= nums[i] <= 2^16.

"""


class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        42ms
        """
        start = 0
        # 一开始就赢了
        for num in nums:
            start ^= num
        if start == 0:
            return True
        else:
        # 否则A要赢只有在A取走一个值之后，给B剩下的奇数个相同的数，此时B没有别的方法，不然B不会被将死
        # 所以到B的时候一定为奇数个数。如果在奇数个数的B没被将死，则A不可能被将死，同上。所以游戏能继续到B只剩一个数或被将死
            if len(nums) % 2 == 0:
                return True
            else:
                return False