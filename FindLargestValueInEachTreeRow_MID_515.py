"""
You need to find the largest value in each row of a binary tree.

Example:

Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        88ms
        """
        self.dicts = []
        if not root:
            return []

        def dfs(root, count):
            if count >= len(self.dicts):
                self.dicts.append(root.val)
            else:
                self.dicts[count] = max(self.dicts[count], root.val)
            if root.left:
                dfs(root.left, count + 1)
            if root.right:
                dfs(root.right, count + 1)

        dfs(root, 0)
        return self.dicts

    def largestValues_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        72ms
        """
        import collections
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        ans = []
        cur = []
        tmp = []
        while queue:
            top = queue.popleft()
            cur.append(top.val)
            if top.left:
                tmp.append(top.left)
            if top.right:
                tmp.append(top.right)
            if not queue:
                ans.append(max(v for v in cur))
                for node in tmp:
                    queue.append(node)
                cur = []
                tmp = []
        return ans

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(Solution().largestValues(root))

root = TreeNode(1)
print(Solution().largestValues(root))

print(Solution().largestValues(None))