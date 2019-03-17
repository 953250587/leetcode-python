"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.


Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
         28 ms
        :param root:
        :return:
        """
        import collections
        adj, q, subRoot = collections.defaultdict(set), {root}, [None]
        while q:
            deepestSet, q = q, {child for node in q for child in (node.left, node.right) if child}

        def dfs(node):
            left, right = node.left and dfs(node.left) or set(), node.right and dfs(node.right) or set()
            curSet = left | right | {node}
            if curSet & deepestSet == deepestSet and subRoot[0] == None:
                subRoot[0] = node
            return curSet

        dfs(root)
        return subRoot[0]
