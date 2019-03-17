"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.



Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:



Note:

1 <= N <= 20
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        128 ms
        """
        if N % 2 == 0:
            return []
        dicts = {}
        dicts[1] = [TreeNode(0)]
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        dicts[3] = [root]
        def create_N_Node(N):
            if N in dicts:
                return dicts[N]
            result = []
            for i in range(1, N - 1, 2):
                left_list = create_N_Node(i)
                right_list = create_N_Node(N - 1 - i)
                for i in left_list:
                    for j in right_list:
                        root = TreeNode(0)
                        root.left = i
                        root.right = j
                        result.append(root)
            dicts[N] = result
            return dicts[N]
        return create_N_Node(N)






class Solution_1(object):
    memo = {0: [], 1: [TreeNode(0)]}
    """
    304ms
    """
    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]