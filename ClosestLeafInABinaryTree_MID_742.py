"""
Given a binary tree where every node has a unique value, and a target key k, find the closest leaf node to target k in the tree.

A node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the closest leaf node to 1.

Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The closest leaf node is the root node itself.

Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.

Note:

    root represents a binary tree with at least 1 node and at most 1000 nodes.
    Every node has a unique node.val in range [1, 1000].
    There exists some node in the given binary tree for which node.val == k.

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        85ms
        """
        self.leaf_info = []
        self.k = k
        self.node_k = None
        self.node_k_info = None
        def dfs(root, count, info):
            info.append([count, root.val])
            if root.val == self.k:
                self.node_k = [count, root]
                self.node_k_info = info[:]
                return
            if root.left:
                dfs(root.left, count + 1, info[:])
            if root.right:
                dfs(root.right, count + 1, info[:])
            if not root.left and not root.right:
                self.leaf_info.append(info)
        dfs(root, 0, [])
        print(self.leaf_info)
        print(self.node_k_info)
        self.min_1 = float('inf')
        self.ans = None
        for leaf in self.leaf_info:
            i = 0
            while leaf[i][1] == self.node_k_info[i][1]:
                i += 1
            a = (leaf[-1][0] - leaf[i - 1][0]) + (self.node_k[0] - leaf[i - 1][0])
            if a < self.min_1:
                self.ans = leaf[-1][1]
                self.min_1 = a

        def dfs_2(root, count):
            if not root.left and not root.right:
                if count < self.min_1:
                    self.ans = root.val
                    self.min_1 = count
                return
            if root.left:
                dfs_2(root.left, count + 1)
            if root.right:
                dfs_2(root.right, count + 1)
        dfs_2(self.node_k[1], 0)
        return self.ans


    def findClosestLeaf_1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        82ms
        """
        def visit(root):
            if not root:
                return [1e9] * 3
            kDists, leafDists, bests = zip(visit(root.left), visit(root.right))
            kDist = 0 if root.val == k else 9999 + min(kDists)
            leafDist = root.val if root.left is root.right else 9999 + min(leafDists)
            return kDist, leafDist, min(kDist + leafDist, *bests)
        return visit(root)[2] % 9999



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
root.left.left.left.left = TreeNode(6)
print(Solution().findClosestLeaf(root, 2))


root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# # root.right.left = TreeNode(7)
# # root.right.right = TreeNode(8)
# root.left.left = TreeNode(4)
# root.left.left.left = TreeNode(5)
# root.left.left.left.left = TreeNode(6)
print(Solution().findClosestLeaf(root, 1))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(8)
# root.left.left = TreeNode(4)
# root.left.left.left = TreeNode(5)
# root.left.left.left.left = TreeNode(6)
print(Solution().findClosestLeaf(root, 1))