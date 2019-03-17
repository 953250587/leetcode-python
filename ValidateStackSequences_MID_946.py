"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        72 ms
        """
        if not pushed and not popped:
            return True
        stack = []
        while popped:
            flag = len(pushed)
            # 不是popped的末尾的时候就往stack添加元素
            for i, val in enumerate(pushed):
                stack.append(val)
                if val == popped[0]:
                    flag = i + 1
                    break
            # 添加的元素更新
            pushed = pushed[flag:]
            # 排除元素
            start = 0
            while start < len(popped) and stack and popped[start] == stack[-1]:
                start += 1
                stack.pop()
            popped = popped[start:]
            # 判断结束时候是否满足要求
            if not pushed:
                return not stack and not popped
        return False

    def validateStackSequences_1(self, pushed, popped):
        """
        28MS
        :param pushed:
        :param popped:
        :return:
        """
        st = []
        while popped:
            if st and popped[0] == st[-1]:
                popped.pop(0)
                st.pop()
            elif pushed:
                st.append(pushed.pop(0))
            else:
                return False
        return True


print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print(Solution().validateStackSequences(pushed = [], popped = []))


