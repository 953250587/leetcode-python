"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        45ms
        """
        import collections
        self.dict = collections.defaultdict(list)
        self.max = 0
        def visit(root, count, i):
            if root == None:
                return
            self.dict[count].append(i)
            self.max = max(self.max, i - self.dict[count][0] + 1)
            if root.left:
                visit(root.left, count + 1, i * 2)
            if root.right:
                visit(root.right, count + 1, i *2 + 1)
        visit(root, 0, 1)
        print(self.dict)
        return self.max

    def widthOfBinaryTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        45ms
        """
        # q = [(root, 0, 0)]
        # cur_depth = left = ans = 0
        # for node, depth, pos in q:
        #     if node:
        #         q.append((node.left, depth+1, pos*2))
        #         q.append((node.right, depth+1, pos*2+1))
        #         if cur_depth != depth:
        #             cur_depth = depth
        #             left = pos
        #         ans = max(ans, pos - left + 1)
        # return ans
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [child
                     for num, node in level
                     for child in enumerate((node.left, node.right), 2 * num)
                     if child[1]]
        return width

    def widthOfBinaryTree_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        42ms
        """
        if not root:
            return 0
        res = 0
        que = [(root, 0)]
        while que:
            next_row = []
            tmp = que[-1][1] - que[0][1] + 1
            res = max(res, tmp)
            for node, index in que:
                if node.left:
                    next_row.append((node.left, index * 2))
                if node.right:
                    next_row.append((node.right, index * 2 + 1))
            que = next_row
        return res
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print(Solution().widthOfBinaryTree(root))


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)

print(Solution().widthOfBinaryTree(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(7)

print(Solution().widthOfBinaryTree(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)

print(Solution().widthOfBinaryTree(root))