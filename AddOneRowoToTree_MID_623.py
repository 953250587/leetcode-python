"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:

Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1

Note:

    The given d is in range [1, maximum depth of the given tree + 1].
    The given binary tree has at least one tree node.

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        72ms
        """
        self.d = d
        self.v = v
        if d == 1:
            new_root = TreeNode(self.v)
            new_root.left = root
            return new_root

        def dfs(root, count):
            if count < d:
                if root.left:
                    dfs(root.left, count + 1)
                if root.right:
                    dfs(root.right, count + 1)
            elif count == d:
                new_root_left = TreeNode(self.v)
                new_root_left.left = root.left
                root.left = new_root_left
                new_root_right = TreeNode(self.v)
                new_root_right.right = root.right
                root.right = new_root_right
        dfs(root, 2)
        return root

    def addOneRow_1(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        65ms
        """

        assert d >= 1, "Invalid 'd'."

        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            cur_depth = 1
            self.addOneRowH(root, v, d, cur_depth)
            return root

    def addOneRowH(self, root, v, d, cur_depth):

        if root is None:
            return

        if cur_depth == (d - 1):

            if root.left:
                new_node = TreeNode(v)
                new_node.left = root.left
                root.left = new_node
            else:
                new_node = TreeNode(v)
                root.left = new_node

            if root.right:
                new_node = TreeNode(v)
                new_node.right = root.right
                root.right = new_node
            else:
                new_node = TreeNode(v)
                root.right = new_node

            return
        else:
            self.addOneRowH(root.left, v, d, cur_depth + 1)
            self.addOneRowH(root.right, v, d, cur_depth + 1)

    def addOneRow_2(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        62ms
        """
        if not root:
            root = TreeNode(v)
            return root
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        s = [[root]]
        cur = root
        count = 1
        while cur and count < d - 1:
            level = s[-1]
            temp = []
            for item in level:
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            s.append(temp)
            count += 1
        level = s[-1]
        for item in level:
            left = item.left
            right = item.right
            nodeL = TreeNode(v)
            nodeR = TreeNode(v)
            item.left = nodeL
            item.right = nodeR
            nodeL.left = left
            nodeR.right = right
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)

def visit(root):
    print(root.val)
    if root.left:
        visit(root.left)
    if root.right:
        visit(root.right)

visit(root)
a = Solution().addOneRow(root, 1, 3)
visit(a)


