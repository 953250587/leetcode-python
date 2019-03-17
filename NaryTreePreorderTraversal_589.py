"""
Given an n-ary tree, return the preorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its preorder traversal as: [1,3,5,6,2,4].


Note: Recursive solution is trivial, could you do it iteratively?


"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        124ms
        """
        start = [root]
        result = []
        while start:
            a = start.pop(0)
            if a:
                result.append(a.val)
                for i, c in enumerate(a.children):
                    start.insert(0 + i, c)
        return result

    def preorder_1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        120ms
        """
        res = []
        if not root: return res

        def preorderHelper(root, res):
            res.append(root.val)
            if not root.children: return
            for child in root.children:
                preorderHelper(child, res)

        preorderHelper(root, res)
        return res
