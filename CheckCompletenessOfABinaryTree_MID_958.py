"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Note:

The tree will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        44 ms
        """
        def isCompleteSubTree(root):
            # print(root.val)
            if not root:
                return 0, 0
            if root:
                left_deep = isCompleteSubTree(root.left)
                right_deep = isCompleteSubTree(root.right)
                print(root.val, left_deep, right_deep)
                if not left_deep or not right_deep:
                    return None
                # 左边有一支比其他都高
                if left_deep[0] > left_deep[1] == right_deep[0] == right_deep[1]:
                    return left_deep[0] + 1, left_deep[1] + 1
                # 左边两支比右边高
                elif left_deep[0] == left_deep[1] > right_deep[0] == right_deep[1]:
                    return left_deep[0] + 1, right_deep[0] + 1
                # 大家一样高
                elif left_deep[0] == left_deep[1] == right_deep[0] == right_deep[1]:
                    return left_deep[0] + 1, left_deep[1] + 1
                # 右边有一支最矮
                elif left_deep[0] == left_deep[1] == right_deep[0] > right_deep[1]:
                    return left_deep[0] + 1, right_deep[1] + 1
                else:
                    return None

        if isCompleteSubTree(root):
            return True
        else:
            return False


    def isCompleteTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        24ms 排序输出查看情况
        """
        if not root:
            return True

        queue = [root]

        missing = False
        while queue:
            cur = queue.pop(0)
            if cur.left:
                if missing:
                    return False
                queue.append(cur.left)
            else:
                missing = True

            if cur.right:
                if missing:
                    return False
                queue.append(cur.right)
            else:
                missing = True

        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
print(Solution().isCompleteTree(root))
