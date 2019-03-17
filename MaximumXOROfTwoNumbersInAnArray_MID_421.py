"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        908ms
        """
        max_num=max(nums)
        s=bin(max_num)[2:]
        two_max_num_len=len(s)
        dicts_nums={}
        help_str='{0:0>' + str(two_max_num_len) + '}'
        lists_max_str=[]

        def add(num):
            dicts=dicts_nums
            add_num=help_str.format((bin(num)[2:]))
            if add_num[0]=='1':
                lists_max_str.append(add_num)
            print(add_num)
            for i in add_num:
                if i not in dicts.keys():
                    dicts[i]={}
                dicts=dicts[i]
            dicts['num']=True

        for num in nums:
            add(num)
        # print(dicts_nums)
        # print(lists_max_str)

        def findprefer(max_str):
            dicts = dicts_nums
            prefer_str=''
            for i in max_str:
                if i=='1' and '0' in dicts.keys():
                    dicts=dicts['0']
                    prefer_str+='1'
                elif i=='1':
                    dicts=dicts['1']
                    prefer_str += '0'
                elif i=='0' and '1' in dicts.keys():
                    dicts = dicts['1']
                    prefer_str += '1'
                elif i=='0':
                    dicts = dicts['0']
                    prefer_str += '0'
            return int(prefer_str, 2)

        max_XOR=0
        for max_str in lists_max_str:
            max_XOR=max(max_XOR,findprefer(max_str))
        return max_XOR

    def findMaximumXOR_1(self, nums):
        """
         118ms
        :param nums:
        :return:
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            print(answer)
            prefixes = {num >> i for num in nums}
            # set判断是否存在为o1
            print(type(prefixes))
            # 从上次的情况出发，位数+1，判断下一位为1的是不是有prefixes中的来个那个元素可以满足
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer



print(Solution().findMaximumXOR_1([3, 10, 5, 25, 2, 8]))