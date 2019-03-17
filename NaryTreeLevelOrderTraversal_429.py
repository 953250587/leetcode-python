"""
即刻前往   |   将我的账号同步到 LeetCode 中国
LeetCode
Explore
Problems
Mock
Contest
Articles
Discuss
 Store
 Premium
New Playground
2
pjq

429. N-ary Tree Level Order Traversal
DescriptionHintsSubmissionsDiscussSolution
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:





We should return its level order traversal:





[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        120ms
        """
        if root == None:
            return []
        start = [root]
        result = []
        while start:
            ans = []
            next_start = []
            for k in start:
                if not k:
                    continue
                ans.append(k.val)
                for i, c in enumerate(k.children):
                    next_start.append(c)
            start = next_start
            result.append(ans)
        return result