"""
Print a binary tree in an m*n 2D string array following these rules:

    The row number m should be equal to the height of the given binary tree.
    The column number n should always be an odd number.
    The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
    Each unused space should contain an empty string "".
    Print the subtrees following the same rules.

Example 1:

Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

Example 3:

Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note: The height of binary tree is in the range of [1, 10].
"""
import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype
        42ms
        """
        if not root:
            return []
        self.max_count = 0
        def visit(root, count):
            self.max_count = max(self.max_count, count)
            if root.left:
                visit(root.left, count + 1)
            if root.right:
                visit(root.right, count + 1)
        visit(root, 1)
        print(self.max_count)
        self.print_t = [[""] * (2 ** self.max_count - 1) for i in range(self.max_count)]

        def mark(root, count, start, end):
            middle = (start + end) // 2
            self.print_t[count][middle] = str(root.val)
            if root.left:
                mark(root.left, count + 1, start, middle - 1)
            if root.right:
                mark(root.right, count + 1, middle + 1, end)
        mark(root, 0, 0, 2 ** self.max_count - 1)
        return self.print_t

    def printTree_1(self, root):
        """
        42ms
        :param root:
        :return:
        """
        if not root: return [""]

        def depth(root):
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1

        d = depth(root)
        self.res = [[""] * (2 ** d - 1) for _ in range(d)]

        def helper(node, d, pos):
            self.res[-d - 1][pos] = str(node.val)
            if node.left: helper(node.left, d - 1, pos - 2 ** (d - 1))
            if node.right: helper(node.right, d - 1, pos + 2 ** (d - 1))

        helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)

print(np.array(Solution().printTree(root)))


root = TreeNode(1)
root.left = TreeNode(2)

print(np.array(Solution().printTree(root)))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print(np.array(Solution().printTree(root)))


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)

print(np.array(Solution().printTree(None)))