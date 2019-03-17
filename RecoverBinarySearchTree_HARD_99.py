"""
 Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        215ms
        """
        root_copy = root
        self.result = []
        def visit(root):
            if root.left:
                visit(root.left)
            self.result.append(root.val)
            if root.right:
                visit(root.right)

        def change(root):
            if root.left:
                change(root.left)
            root.val = self.result[self.start]
            self.start += 1
            if root.right:
                change(root.right)
        visit(root)
        print(self.result)
        self.result = sorted(self.result)
        self.start = 0
        change(root_copy)

    def recoverTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        125ms
        """
        root_copy = root
        self.temp = None
        self.result = []
        def visit(root):
            if root.left:
                visit(root.left)
            if not self.temp:
                self.temp = root
            else:
                if root.val < self.temp.val:
                    self.result.extend([self.temp, root])
                self.temp = root
            if root.right:
                visit(root.right)

        # def change(root):
        #     if root.left:
        #         change(root.left)
        #     root.val = self.result[self.start]
        #     self.start += 1
        #     if root.right:
        #         change(root.right)
        visit(root)
        print(self.result)
        self.result[0].val, self.result[-1].val = self.result[-1].val, self.result[0].val
        # self.result = sorted(self.result)
        # self.start = 0
        # change(root_copy)

    def recoverTree_2(self, root):
        """
        132ms
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # average O(lgn) space (worst case O(n) space), iteratively, one-pass
        res, stack, first, second = None, [], None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            # first time occurs reversed order
            if res and res.val > node.val:
                if not first:
                    first = res
                # first or second time occurs reversed order
                second = node
            res = node
            root = node.right
        first.val, second.val = second.val, first.val


root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(5)
root.right.right = TreeNode(10)
root_copy = root
Solution().recoverTree_1(root)
def visit(root):
    if root.left:
        print('l')
        visit(root.left)
    print(root.val)
    if root.right:
        print('r')
        visit(root.right)
visit(root_copy)


root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)
root_copy = root
Solution().recoverTree_1(root)
visit(root_copy)